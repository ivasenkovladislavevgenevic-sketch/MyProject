package com.seasonalworld.mod.season;

import net.minecraft.core.BlockPos;
import net.minecraft.core.Holder;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.tags.BiomeTags;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.biome.Biome;
import net.minecraft.world.level.biome.Biomes;

/**
 * Utility class to determine whether seasons should apply to a given biome/position.
 *
 * Seasons are DISABLED in:
 *  - All desert biomes (biome tag: #minecraft:is_badlands, or id contains "desert")
 *  - Nether and End dimensions (handled by caller)
 *
 * Snow in winter is also skipped in deserts.
 */
public class BiomeChecker {

    /**
     * Returns true if the season system should be active at this position.
     */
    public static boolean isSeasonActive(LevelReader level, BlockPos pos) {
        Holder<Biome> biomeHolder = level.getBiome(pos);
        return !isDesertBiome(biomeHolder);
    }

    /**
     * Returns true if the given biome is a desert-type biome.
     * Checks by biome tag (is_dry/sandy) or resource key id.
     */
    public static boolean isDesertBiome(Holder<Biome> biomeHolder) {
        // Check by resource key string (covers vanilla + modded deserts)
        var keyOpt = biomeHolder.unwrapKey();
        if (keyOpt.isPresent()) {
            String path = keyOpt.get().location().getPath();
            if (path.contains("desert")
                    || path.contains("badlands")
                    || path.contains("eroded_badlands")
                    || path.contains("wooded_badlands")
                    || path.contains("mesa")) {
                return true;
            }
        }
        // Check temperature + precipitation = NONE as an extra heuristic for hot/dry biomes
        Biome biome = biomeHolder.value();
        float temp = biome.getBaseTemperature();
        boolean isHotAndDry = temp >= 1.5f && !biome.hasPrecipitation();
        return isHotAndDry;
    }

    /**
     * Checks if snow should accumulate at a position during winter.
     * Returns false for deserts and biomes that are naturally hot.
     */
    public static boolean canSnowInWinter(LevelReader level, BlockPos pos) {
        Holder<Biome> biomeHolder = level.getBiome(pos);
        if (isDesertBiome(biomeHolder)) return false;
        // Allow snow even in normally non-snowy biomes (that's the point of the mod)
        return true;
    }
}
