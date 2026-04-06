package com.customseasons.handler;

import com.customseasons.color.SeasonColors;
import com.customseasons.network.ClientSeasonHolder;
import com.customseasons.season.SeasonType;
import com.customseasons.util.BiomeSeasonHelper;
import net.minecraft.client.color.block.BlockColor;
import net.minecraft.core.BlockPos;
import net.minecraft.core.Holder;
import net.minecraft.world.level.BlockAndTintGetter;
import net.minecraft.world.level.biome.Biome;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.client.event.RegisterColorHandlersEvent;

@EventBusSubscriber(modid = "customseasons", bus = EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public class ClientColorHandler {

    @SubscribeEvent
    public static void onRegisterBlockColors(RegisterColorHandlersEvent.Block event) {
        BlockColor seasonColor = new SeasonBlockColor();

        event.register(seasonColor,
                Blocks.GRASS_BLOCK,
                Blocks.FERN,
                Blocks.LARGE_FERN,
                Blocks.POTTED_FERN,
                Blocks.OAK_LEAVES,
                Blocks.BIRCH_LEAVES,
                Blocks.SPRUCE_LEAVES,
                Blocks.JUNGLE_LEAVES,
                Blocks.ACACIA_LEAVES,
                Blocks.DARK_OAK_LEAVES,
                Blocks.MANGROVE_LEAVES,
                Blocks.CHERRY_LEAVES,
                Blocks.AZALEA_LEAVES,
                Blocks.FLOWERING_AZALEA_LEAVES,
                Blocks.VINE,
                Blocks.TALL_GRASS,
                Blocks.SHORT_GRASS
        );
    }

    private static class SeasonBlockColor implements BlockColor {
        @Override
        public int getColor(BlockState state, BlockAndTintGetter level, BlockPos pos, int tintIndex) {
            SeasonType season = ClientSeasonHolder.getCurrentSeason();

            if (season == null) return -1;

            // In summer, return -1 to use vanilla colors
            if (season == SeasonType.SUMMER) return -1;

            if (pos != null && level != null) {
                Holder<Biome> biome = level.getBiome(pos);
                if (BiomeSeasonHelper.isDesert(biome)) {
                    return -1; // Vanilla color in deserts
                }
            }

            // Use grass color for grass/fern, foliage color for leaves
            boolean isLeaves = state.is(Blocks.OAK_LEAVES)
                    || state.is(Blocks.BIRCH_LEAVES)
                    || state.is(Blocks.SPRUCE_LEAVES)
                    || state.is(Blocks.JUNGLE_LEAVES)
                    || state.is(Blocks.ACACIA_LEAVES)
                    || state.is(Blocks.DARK_OAK_LEAVES)
                    || state.is(Blocks.MANGROVE_LEAVES)
                    || state.is(Blocks.CHERRY_LEAVES)
                    || state.is(Blocks.AZALEA_LEAVES)
                    || state.is(Blocks.FLOWERING_AZALEA_LEAVES);

            if (isLeaves) {
                return SeasonColors.getFoliageColor(season);
            } else {
                return SeasonColors.getGrassColor(season);
            }
        }
    }
}
