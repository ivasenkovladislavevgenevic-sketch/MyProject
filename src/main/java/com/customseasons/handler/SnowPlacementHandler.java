package com.customseasons.handler;

import com.customseasons.season.SeasonManager;
import com.customseasons.season.SeasonType;
import com.customseasons.util.BiomeSeasonHelper;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Holder;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.biome.Biome;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.chunk.LevelChunk;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.level.ChunkEvent;
import net.neoforged.neoforge.event.tick.LevelTickEvent;

import java.util.ArrayList;
import java.util.List;

@EventBusSubscriber(modid = "customseasons", bus = EventBusSubscriber.Bus.GAME)
public class SnowPlacementHandler {

    private static int tickCounter = 0;
    // Process N chunks per tick to avoid lag spikes
    private static final int CHUNKS_PER_TICK = 4;
    // Period in ticks between full passes
    private static final int TICK_PERIOD = 200;

    // Queue for bulk processing on season change
    private static final List<ChunkPos> pendingChunks = new ArrayList<>();
    private static ServerLevel pendingLevel = null;
    private static boolean pendingIsWinter = false;

    @SubscribeEvent
    public static void onChunkLoad(ChunkEvent.Load event) {
        if (!(event.getLevel() instanceof ServerLevel level)) return;
        if (!level.dimension().equals(net.minecraft.world.level.Level.OVERWORLD)) return;
        if (!(event.getChunk() instanceof LevelChunk chunk)) return;

        SeasonType season = SeasonManager.getSeason(level);
        if (season == SeasonType.WINTER) {
            placeSnowInChunk(level, chunk);
        }
    }

    @SubscribeEvent
    public static void onLevelTick(LevelTickEvent.Post event) {
        if (!(event.getLevel() instanceof ServerLevel level)) return;
        if (!level.dimension().equals(net.minecraft.world.level.Level.OVERWORLD)) return;

        // Process pending queue from season change
        if (pendingLevel == level && !pendingChunks.isEmpty()) {
            int processed = 0;
            while (!pendingChunks.isEmpty() && processed < CHUNKS_PER_TICK) {
                ChunkPos pos = pendingChunks.remove(pendingChunks.size() - 1);
                LevelChunk chunk = level.getChunkSource().getChunkNow(pos.x, pos.z);
                if (chunk != null) {
                    if (pendingIsWinter) placeSnowInChunk(level, chunk);
                    else removeSnowInChunk(level, chunk);
                }
                processed++;
            }
            return;
        }

        // Periodic maintenance pass
        if (++tickCounter < TICK_PERIOD) return;
        tickCounter = 0;

        SeasonType season = SeasonManager.getSeason(level);
        if (season != SeasonType.WINTER) return;

        // Iterate all loaded chunks via forced chunk list
        for (LevelChunk chunk : level.getChunkSource().getLoadedChunksIterable()) {
            placeSnowInChunk(level, chunk);
        }
    }

    /**
     * Called when season changes. Queues all loaded chunks for processing.
     */
    public static void onSeasonChange(ServerLevel level, SeasonType newSeason) {
        pendingLevel = level;
        pendingIsWinter = newSeason == SeasonType.WINTER;
        pendingChunks.clear();

        for (LevelChunk chunk : level.getChunkSource().getLoadedChunksIterable()) {
            pendingChunks.add(chunk.getPos());
        }
    }

    /**
     * Places snow layers in a chunk during winter.
     * Skips desert biomes. Places snow even under trees (no sky-light check).
     * Freezes water to ice.
     */
    static void placeSnowInChunk(ServerLevel level, LevelChunk chunk) {
        ChunkPos chunkPos = chunk.getPos();
        int minX = chunkPos.getMinBlockX();
        int minZ = chunkPos.getMinBlockZ();
        int maxX = chunkPos.getMaxBlockX();
        int maxZ = chunkPos.getMaxBlockZ();
        int maxY = level.getMaxBuildHeight() - 1;
        int minY = level.getMinBuildHeight();

        for (int x = minX; x <= maxX; x++) {
            for (int z = minZ; z <= maxZ; z++) {
                BlockPos columnTop = new BlockPos(x, maxY, z);
                Holder<Biome> biome = level.getBiome(columnTop);

                // Skip desert/hot biomes
                if (BiomeSeasonHelper.isDesert(biome)) continue;

                // Find the topmost solid block from the top down
                for (int y = maxY; y >= minY; y--) {
                    BlockPos pos = new BlockPos(x, y, z);
                    BlockState state = level.getBlockState(pos);

                    // Freeze water
                    if (state.is(Blocks.WATER)) {
                        level.setBlockAndUpdate(pos, Blocks.ICE.defaultBlockState());
                        break;
                    }

                    // Skip air, snow layers already placed, leaves (transparent), etc.
                    // We want to find the FIRST solid landing surface
                    if (state.isAir()) continue;

                    // Skip snow we already placed (don't stack infinitely)
                    if (state.is(Blocks.SNOW)) break;

                    // Check if block above is air (place snow there)
                    BlockPos above = pos.above();
                    BlockState aboveState = level.getBlockState(above);
                    if (aboveState.isAir()) {
                        level.setBlockAndUpdate(above, Blocks.SNOW.defaultBlockState());
                    }
                    break;
                }
            }
        }
    }

    /**
     * Removes snow layers and melts ice back to water in a chunk.
     */
    static void removeSnowInChunk(ServerLevel level, LevelChunk chunk) {
        ChunkPos chunkPos = chunk.getPos();
        int minX = chunkPos.getMinBlockX();
        int minZ = chunkPos.getMinBlockZ();
        int maxX = chunkPos.getMaxBlockX();
        int maxZ = chunkPos.getMaxBlockZ();
        int maxY = level.getMaxBuildHeight() - 1;
        int minY = level.getMinBuildHeight();

        for (int x = minX; x <= maxX; x++) {
            for (int z = minZ; z <= maxZ; z++) {
                for (int y = maxY; y >= minY; y--) {
                    BlockPos pos = new BlockPos(x, y, z);
                    BlockState state = level.getBlockState(pos);

                    if (state.is(Blocks.SNOW)) {
                        level.setBlockAndUpdate(pos, Blocks.AIR.defaultBlockState());
                    } else if (state.is(Blocks.ICE)) {
                        level.setBlockAndUpdate(pos, Blocks.WATER.defaultBlockState());
                    }
                }
            }
        }
    }
}
