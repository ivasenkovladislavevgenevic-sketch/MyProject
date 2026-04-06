package com.customseasons.season;

import com.customseasons.handler.SnowPlacementHandler;
import com.customseasons.network.SeasonSyncPacket;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.neoforged.neoforge.network.PacketDistributor;

public class SeasonManager {

    public static final int DAYS_PER_SEASON = 7;
    private static final String SAVE_KEY = "customseasons_data";

    public static SeasonSavedData getData(ServerLevel level) {
        return level.getDataStorage().computeIfAbsent(SeasonSavedData.factory(), SAVE_KEY);
    }

    public static SeasonType getSeason(ServerLevel level) {
        return getData(level).getCurrentSeason();
    }

    /**
     * Called every server tick. Advances season by tracking day transitions.
     */
    public static void tick(ServerLevel level) {
        long currentDay = level.getDayTime() / 24000L;
        SeasonSavedData data = getData(level);

        if (data.getLastDay() < 0) {
            data.setLastDay(currentDay);
            return;
        }

        if (currentDay > data.getLastDay()) {
            data.setLastDay(currentDay);
            data.incrementDayCount();

            if (data.getDayCount() >= DAYS_PER_SEASON) {
                SeasonType oldSeason = data.getCurrentSeason();
                SeasonType newSeason = oldSeason.next();
                data.setCurrentSeason(newSeason);
                data.resetDayCount();

                // Sync to all players
                syncToAll(level, newSeason);

                // Handle snow placement/removal
                boolean wasWinter = oldSeason == SeasonType.WINTER;
                boolean isWinter = newSeason == SeasonType.WINTER;
                if (wasWinter != isWinter) {
                    SnowPlacementHandler.onSeasonChange(level, newSeason);
                }
            }
        }
    }

    public static void syncToAll(ServerLevel level, SeasonType season) {
        SeasonSyncPacket packet = new SeasonSyncPacket(season);
        for (ServerPlayer player : level.getServer().getPlayerList().getPlayers()) {
            PacketDistributor.sendToPlayer(player, packet);
        }
    }

    /** Force-set season (used by command) */
    public static void setSeason(ServerLevel level, SeasonType season) {
        SeasonSavedData data = getData(level);
        data.setCurrentSeason(season);
        data.resetDayCount();
        syncToAll(level, season);
        SnowPlacementHandler.onSeasonChange(level, season);
    }
}
