package com.seasonalworld.mod.mixin;

import com.seasonalworld.mod.client.SeasonColorClient;
import com.seasonalworld.mod.season.Season;
import net.minecraft.client.renderer.BiomeColors;
import net.minecraft.world.level.FoliageColor;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/**
 * Overrides foliage color based on the current season.
 *
 * SPRING  — slightly pale green
 * SUMMER  — rich green (vanilla-like)
 * AUTUMN  — red-yellow
 * WINTER  — near-white pale green (leaves look frost-covered)
 */
@Mixin(FoliageColor.class)
public class MixinFoliageColor {

    @Inject(method = "get(DD)I", at = @At("RETURN"), cancellable = true)
    private static void seasonalFoliageColor(double temperature, double humidity,
                                              CallbackInfoReturnable<Integer> cir) {
        Season season = SeasonColorClient.getCurrentSeason();
        if (season == null) return;

        int base = cir.getReturnValue();
        int seasonal = blendColor(base, season.foliageColor, getBlendFactor(season));
        cir.setReturnValue(seasonal);
    }

    /**
     * Blends two RGB colors.
     * factor=0.0 → fully original, factor=1.0 → fully seasonal
     */
    private static int blendColor(int original, int target, float factor) {
        int r1 = (original >> 16) & 0xFF;
        int g1 = (original >> 8) & 0xFF;
        int b1 = original & 0xFF;
        int r2 = (target >> 16) & 0xFF;
        int g2 = (target >> 8) & 0xFF;
        int b2 = target & 0xFF;
        int r = (int) (r1 + (r2 - r1) * factor);
        int g = (int) (g1 + (g2 - g1) * factor);
        int b = (int) (b1 + (b2 - b1) * factor);
        return (r << 16) | (g << 8) | b;
    }

    /** How strongly the seasonal color overrides the biome color. */
    private static float getBlendFactor(Season season) {
        return switch (season) {
            case SPRING -> 0.65f;
            case SUMMER -> 0.45f;  // Closest to vanilla, slight enhancement
            case AUTUMN -> 0.85f;  // Strong override
            case WINTER -> 0.90f;  // Very strong — pale/white
        };
    }
}
