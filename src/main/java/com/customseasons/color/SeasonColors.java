package com.customseasons.color;

import com.customseasons.season.SeasonType;

public class SeasonColors {

    // Foliage (leaves) colors per season
    public static int getFoliageColor(SeasonType season) {
        return switch (season) {
            case SPRING -> 0x7FBF6A;  // Бледно-зелёный
            case SUMMER -> 0x4CBF5F;  // Насыщенный зелёный
            case AUTUMN -> 0xD4882A;  // Красно-жёлтый
            case WINTER -> 0xC8DCC8;  // Очень бледный зелёно-белый
        };
    }

    // Grass / fern colors per season
    public static int getGrassColor(SeasonType season) {
        return switch (season) {
            case SPRING -> 0x91C96A;  // Весна: чуть бледнее обычного
            case SUMMER -> 0x55C44F;  // Лето: насыщенный
            case AUTUMN -> 0xC4922A;  // Осень: красно-жёлтый
            case WINTER -> 0xD0DDD0;  // Зима: очень бледный
        };
    }
}
