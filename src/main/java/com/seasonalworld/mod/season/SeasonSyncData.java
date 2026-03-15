package com.seasonalworld.mod.season;

import net.minecraft.nbt.CompoundTag;

/**
 * Persisted per-world season state, saved in level.dat extra data.
 */
public class SeasonSyncData {

    private Season currentSeason;
    private long seasonStartDay;

    public SeasonSyncData() {
        this.currentSeason = Season.SPRING;
        this.seasonStartDay = 0;
    }

    public Season getCurrentSeason() {
        return currentSeason;
    }

    public void setCurrentSeason(Season season) {
        this.currentSeason = season;
    }

    public long getSeasonStartDay() {
        return seasonStartDay;
    }

    public void setSeasonStartDay(long day) {
        this.seasonStartDay = day;
    }

    public CompoundTag save() {
        CompoundTag tag = new CompoundTag();
        tag.putString("season", currentSeason.name());
        tag.putLong("seasonStartDay", seasonStartDay);
        return tag;
    }

    public static SeasonSyncData load(CompoundTag tag) {
        SeasonSyncData data = new SeasonSyncData();
        if (tag.contains("season")) {
            try {
                data.currentSeason = Season.valueOf(tag.getString("season").toUpperCase());
            } catch (IllegalArgumentException e) {
                data.currentSeason = Season.SPRING;
            }
        }
        if (tag.contains("seasonStartDay")) {
            data.seasonStartDay = tag.getLong("seasonStartDay");
        }
        return data;
    }
}
