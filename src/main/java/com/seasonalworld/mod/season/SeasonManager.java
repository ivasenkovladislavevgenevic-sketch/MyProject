package com.seasonalworld.mod.season;

import com.seasonalworld.mod.SeasonalWorldMod;
import com.seasonalworld.mod.config.SeasonConfig;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.GameRules;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

/**
 * Central manager that tracks and advances seasons per dimension.
 *
 * Season length is configurable via SeasonConfig.SEASON_DURATION_DAYS.
 * One Minecraft day = 24000 ticks.
 */
public class SeasonManager {

    /** Maps dimension UUID to current season. */
    private static final Map<UUID, Season> dimensionSeasons = new HashMap<>();

    /** Tracks how many ticks have passed in the current season for each dimension. */
    private static final Map<UUID, Long> seasonProgress = new HashMap<>();

    public static void init() {
        SeasonalWorldMod.LOGGER.info("[SeasonalWorld] SeasonManager ready.");
    }

    /**
     * Called every server tick for a given level.
     * Advances season when enough days have elapsed.
     */
    public static void onServerTick(ServerLevel level) {
        UUID dimId = level.dimension().location().hashCode() + "_" + level.getSeed() != null
                ? UUID.nameUUIDFromBytes((level.dimension().location().toString() + level.getSeed()).getBytes())
                : UUID.randomUUID();

        long dayTime = level.getDayTime() % 24000L;
        long totalDays = level.getDayTime() / 24000L;

        int daysPerSeason = SeasonConfig.SEASON_DURATION_DAYS.get();
        int totalSeasonIndex = (int) (totalDays / daysPerSeason);
        Season newSeason = Season.values()[totalSeasonIndex % Season.values().length];

        Season current = dimensionSeasons.get(dimId);
        if (current != newSeason) {
            dimensionSeasons.put(dimId, newSeason);
            SeasonalWorldMod.LOGGER.info("[SeasonalWorld] Season changed to {} in dimension {}",
                    newSeason, level.dimension().location());
        }
    }

    /** Returns the current season for the given level. Defaults to SPRING if unknown. */
    public static Season getCurrentSeason(ServerLevel level) {
        UUID dimId = UUID.nameUUIDFromBytes(
                (level.dimension().location().toString() + level.getSeed()).getBytes());
        return dimensionSeasons.getOrDefault(dimId, computeSeasonFromTime(level));
    }

    /**
     * Computes season purely from world time — no state needed.
     * Used both as a fallback and for client-side estimation.
     */
    public static Season computeSeasonFromTime(ServerLevel level) {
        int daysPerSeason = SeasonConfig.SEASON_DURATION_DAYS.get();
        long totalDays = level.getDayTime() / 24000L;
        int idx = (int) ((totalDays / daysPerSeason) % Season.values().length);
        return Season.values()[idx];
    }

    /**
     * Fraction [0.0, 1.0) of how far through the current season we are.
     * Useful for smooth color blending.
     */
    public static float getSeasonProgress(ServerLevel level) {
        int daysPerSeason = SeasonConfig.SEASON_DURATION_DAYS.get();
        long totalDays = level.getDayTime() / 24000L;
        long dayInSeason = totalDays % daysPerSeason;
        return (float) dayInSeason / (float) daysPerSeason;
    }
}
