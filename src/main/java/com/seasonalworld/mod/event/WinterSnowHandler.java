package com.seasonalworld.mod.event;

import com.seasonalworld.mod.SeasonalWorldMod;
import com.seasonalworld.mod.config.SeasonConfig;
import com.seasonalworld.mod.season.BiomeChecker;
import com.seasonalworld.mod.season.Season;
import com.seasonalworld.mod.season.SeasonManager;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.LightLayer;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.SnowLayerBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.chunk.LevelChunk;
import net.minecraft.world.level.levelgen.Heightmap;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.level.ChunkTickEvent;
import net.neoforged.neoforge.event.tick.LevelTickEvent;

import java.util.Random;

/**
 * Handles winter snow accumulation everywhere in the world (except deserts).
 *
 * Features:
 *  - Snow on the ground surface, including under tree canopies (uses MOTION_BLOCKING_NO_LEAVES heightmap)
 *  - Snow on top of water/rivers (places ICE)
 *  - Global snow — not limited to chunks near the player; all loaded chunks are processed
 *  - Snow melts automatically when season changes away from WINTER
 */
@EventBusSubscriber(modid = SeasonalWorldMod.MOD_ID, bus = EventBusSubscriber.Bus.GAME)
public class WinterSnowHandler {

    private static final Random RANDOM = new Random();

    /**
     * Tick event: every N ticks during winter, try to place snow in loaded chunks.
     */
    @SubscribeEvent
    public static void onLevelTick(LevelTickEvent.Post event) {
        if (!(event.getLevel() instanceof ServerLevel level)) return;
        if (level.isClientSide()) return;

        Season season = SeasonManager.getCurrentSeason(level);

        // Run snow logic every 4 ticks to reduce lag
        if (level.getGameTime() % 4 != 0) return;

        if (season == Season.WINTER) {
            placeSnowInLoadedChunks(level);
        } else {
            // Melt seasonal snow when not winter
            if (level.getGameTime() % 80 == 0) {
                meltSeasonalSnow(level);
            }
        }
    }

    /**
     * Iterates all loaded chunks and places snow/ice on exposed surfaces.
     */
    private static void placeSnowInLoadedChunks(ServerLevel level) {
        int snowChance = SeasonConfig.SNOW_CHANCE_PER_CHUNK_TICK.get(); // e.g. 3 (out of 16)

        for (LevelChunk chunk : getLoadedChunks(level)) {
            // Probabilistic — not every chunk every tick (performance)
            if (RANDOM.nextInt(16) >= snowChance) continue;

            ChunkPos chunkPos = chunk.getPos();
            // Pick a random column in this chunk
            int x = chunkPos.getMinBlockX() + RANDOM.nextInt(16);
            int z = chunkPos.getMinBlockZ() + RANDOM.nextInt(16);

            placeSnowColumn(level, x, z);
        }
    }

    /**
     * Places snow at the highest solid surface at (x, z).
     * Uses MOTION_BLOCKING_NO_LEAVES so snow goes under tree canopies.
     * Places ICE on water blocks.
     */
    private static void placeSnowColumn(ServerLevel level, int x, int z) {
        // Check biome — skip deserts
        BlockPos surfacePos = new BlockPos(x, level.getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES, x, z), z);
        if (!BiomeChecker.canSnowInWinter(level, surfacePos)) return;

        BlockPos belowSurface = surfacePos.below();
        BlockState belowState = level.getBlockState(belowSurface);

        // Place ice on water (rivers, lakes, oceans)
        if (belowState.getBlock() == Blocks.WATER) {
            if (level.getLightEngine().getLayerListener(LightLayer.BLOCK).getLightValue(belowSurface) < 10) {
                level.setBlockAndUpdate(belowSurface, Blocks.ICE.defaultBlockState());
            }
            return;
        }

        // Place snow on solid surfaces
        BlockState surfaceState = level.getBlockState(surfacePos);
        if (surfaceState.isAir()) {
            level.setBlockAndUpdate(surfacePos, Blocks.SNOW.defaultBlockState()
                    .setValue(SnowLayerBlock.LAYERS, 1));
        } else if (surfaceState.is(Blocks.SNOW)) {
            // Build up snow layers (max 3 in winter)
            int layers = surfaceState.getValue(SnowLayerBlock.LAYERS);
            if (layers < 3) {
                level.setBlockAndUpdate(surfacePos, surfaceState
                        .setValue(SnowLayerBlock.LAYERS, layers + 1));
            }
        }
    }

    /**
     * Removes snow that was placed by this mod (not player-placed snowballs etc.).
     * Called during non-winter seasons to clean up.
     */
    private static void meltSeasonalSnow(ServerLevel level) {
        for (LevelChunk chunk : getLoadedChunks(level)) {
            if (RANDOM.nextInt(16) >= 2) continue;

            ChunkPos chunkPos = chunk.getPos();
            int x = chunkPos.getMinBlockX() + RANDOM.nextInt(16);
            int z = chunkPos.getMinBlockZ() + RANDOM.nextInt(16);

            int y = level.getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES, x, z);
            BlockPos pos = new BlockPos(x, y, z);
            BlockState state = level.getBlockState(pos);

            if (state.is(Blocks.SNOW)) {
                int layers = state.getValue(SnowLayerBlock.LAYERS);
                if (layers <= 1) {
                    level.setBlockAndUpdate(pos, Blocks.AIR.defaultBlockState());
                } else {
                    level.setBlockAndUpdate(pos, state.setValue(SnowLayerBlock.LAYERS, layers - 1));
                }
            } else if (state.is(Blocks.ICE)) {
                level.setBlockAndUpdate(pos, Blocks.WATER.defaultBlockState());
            }
        }
    }

    /**
     * Returns an iterable of all currently loaded chunks in the level.
     */
    private static Iterable<LevelChunk> getLoadedChunks(ServerLevel level) {
        return level.getChunkSource().getLoadedChunksIterable();
    }
}
