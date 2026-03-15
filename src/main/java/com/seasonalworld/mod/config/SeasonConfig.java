package com.seasonalworld.mod.config;

import net.neoforged.neoforge.common.ModConfigSpec;

/**
 * Common (server-side) config for SeasonalWorld.
 *
 * Config file: config/seasonalworld-common.toml
 */
public class SeasonConfig {

    public static final ModConfigSpec SPEC;

    /** How many in-game days each season lasts. Default: 7 days. */
    public static final ModConfigSpec.IntValue SEASON_DURATION_DAYS;

    /**
     * Probability weight for snow placement per chunk per tick during winter.
     * Higher = more snow placed per tick. Range: 1–16. Default: 4.
     */
    public static final ModConfigSpec.IntValue SNOW_CHANCE_PER_CHUNK_TICK;

    /** If true, ice forms on rivers and lakes in winter. Default: true. */
    public static final ModConfigSpec.BooleanValue FREEZE_WATER_IN_WINTER;

    /** If true, snow accumulates under tree canopies. Default: true. */
    public static final ModConfigSpec.BooleanValue SNOW_UNDER_TREES;

    static {
        ModConfigSpec.Builder builder = new ModConfigSpec.Builder();

        builder.comment("Seasonal World Configuration").push("seasons");

        SEASON_DURATION_DAYS = builder
                .comment("Number of in-game days per season (1 MC day = 24000 ticks). Default: 7")
                .defineInRange("seasonDurationDays", 7, 1, 365);

        SNOW_CHANCE_PER_CHUNK_TICK = builder
                .comment("Snow placement chance per loaded chunk per 4 ticks in winter. Range 1-16. Default: 4")
                .defineInRange("snowChancePerChunkTick", 4, 1, 16);

        FREEZE_WATER_IN_WINTER = builder
                .comment("Freeze rivers, lakes, and oceans in winter. Default: true")
                .define("freezeWaterInWinter", true);

        SNOW_UNDER_TREES = builder
                .comment("Snow accumulates under tree canopies in winter. Default: true")
                .define("snowUnderTrees", true);

        builder.pop();
        SPEC = builder.build();
    }
}
