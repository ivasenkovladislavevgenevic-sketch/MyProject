package com.customseasons.season;

public enum SeasonType {
    SPRING,
    SUMMER,
    AUTUMN,
    WINTER;

    public SeasonType next() {
        return values()[(ordinal() + 1) % 4];
    }

    public String getTranslationKey() {
        return "season.customseasons." + name().toLowerCase();
    }

    public static SeasonType fromId(int id) {
        SeasonType[] vals = values();
        return vals[id % vals.length];
    }
}
