package com.customseasons.season;

import net.minecraft.nbt.CompoundTag;
import net.minecraft.world.level.saveddata.SavedData;

public class SeasonSavedData extends SavedData {

    private static final String KEY_SEASON = "season";
    private static final String KEY_DAY_COUNT = "dayCount";
    private static final String KEY_LAST_DAY = "lastDay";

    private SeasonType currentSeason = SeasonType.SPRING;
    private int dayCount = 0;
    private long lastDay = -1L;

    public SeasonSavedData() {}

    public static SeasonSavedData load(CompoundTag tag) {
        SeasonSavedData data = new SeasonSavedData();
        data.currentSeason = SeasonType.fromId(tag.getInt(KEY_SEASON));
        data.dayCount = tag.getInt(KEY_DAY_COUNT);
        data.lastDay = tag.getLong(KEY_LAST_DAY);
        return data;
    }

    @Override
    public CompoundTag save(CompoundTag tag) {
        tag.putInt(KEY_SEASON, currentSeason.ordinal());
        tag.putInt(KEY_DAY_COUNT, dayCount);
        tag.putLong(KEY_LAST_DAY, lastDay);
        return tag;
    }

    public static SavedData.Factory<SeasonSavedData> factory() {
        return new SavedData.Factory<>(SeasonSavedData::new, SeasonSavedData::load, null);
    }

    public SeasonType getCurrentSeason() {
        return currentSeason;
    }

    public void setCurrentSeason(SeasonType season) {
        this.currentSeason = season;
        setDirty();
    }

    public int getDayCount() {
        return dayCount;
    }

    public void incrementDayCount() {
        this.dayCount++;
        setDirty();
    }

    public void resetDayCount() {
        this.dayCount = 0;
        setDirty();
    }

    public long getLastDay() {
        return lastDay;
    }

    public void setLastDay(long day) {
        this.lastDay = day;
        setDirty();
    }
}
