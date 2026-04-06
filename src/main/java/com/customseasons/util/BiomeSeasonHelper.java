package com.customseasons.util;

import com.customseasons.season.SeasonType;
import net.minecraft.core.Holder;
import net.minecraft.tags.BiomeTags;
import net.minecraft.world.level.biome.Biome;

public class BiomeSeasonHelper {

    private static final float DESERT_TEMP_THRESHOLD = 0.95f;

    /**
     * Returns true if the biome should be excluded from seasonal effects
     * (deserts and other hot/dry biomes).
     */
    public static boolean isDesert(Holder<Biome> biome) {
        return biome.is(BiomeTags.IS_SANDY)
                || biome.is(BiomeTags.IS_DRY)
                || biome.value().getBaseTemperature() > DESERT_TEMP_THRESHOLD;
    }

    /**
     * Returns true if winter effects (snow, ice) should apply to this biome.
     */
    public static boolean shouldHaveWinterEffects(Holder<Biome> biome, SeasonType season) {
        return season == SeasonType.WINTER && !isDesert(biome);
    }
}
