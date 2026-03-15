package com.seasonalworld.mod.season;

/**
 * Represents the four seasons. Each season has a foliage color and grass color tint.
 *
 * Foliage colors:
 *   SPRING  — slightly pale green
 *   SUMMER  — rich green
 *   AUTUMN  — red-yellow
 *   WINTER  — pale pale green + white overlay (handled separately)
 */
public enum Season {
    SPRING("spring", 0x85B35A, 0x79B050),  // pale greenish
    SUMMER("summer", 0x48B518, 0x3CB018),  // vivid green
    AUTUMN("autumn", 0xC87828, 0xD4881C),  // red-yellow
    WINTER("winter", 0xB8C8A8, 0xBACAAA);  // pale pale green / near-white

    public final String name;
    /** Base foliage color (used in biome color mixin) */
    public final int foliageColor;
    /** Base grass color */
    public final int grassColor;

    Season(String name, int foliageColor, int grassColor) {
        this.name = name;
        this.foliageColor = foliageColor;
        this.grassColor = grassColor;
    }

    /** Returns the next season in the cycle. */
    public Season next() {
        return values()[(ordinal() + 1) % values().length];
    }

    @Override
    public String toString() {
        return name;
    }
}
