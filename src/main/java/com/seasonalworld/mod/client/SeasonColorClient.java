package com.seasonalworld.mod.client;

import com.seasonalworld.mod.season.Season;

/**
 * Client-side singleton that holds the current season received from the server.
 * Updated via network packet when season changes.
 */
public class SeasonColorClient {

    private static Season currentSeason = Season.SPRING;

    public static Season getCurrentSeason() {
        return currentSeason;
    }

    public static void setCurrentSeason(Season season) {
        currentSeason = season;
    }
}
