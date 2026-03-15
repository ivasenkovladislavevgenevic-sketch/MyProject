package com.seasonalworld.mod.mixin;

import com.seasonalworld.mod.client.SeasonColorClient;
import com.seasonalworld.mod.season.Season;
import net.minecraft.world.level.GrassColor;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/**
 * Overrides grass color based on current season.
 */
@Mixin(GrassColor.class)
public class MixinGrassColor {

    @Inject(method = "get(DD)I", at = @At("RETURN"), cancellable = true)
    private static void seasonalGrassColor(double temperature, double humidity,
                                            CallbackInfoReturnable<Integer> cir) {
        Season season = SeasonColorClient.getCurrentSeason();
        if (season == null) return;

        int base = cir.getReturnValue();
        int seasonal = blendColor(base, season.grassColor, getBlendFactor(season));
        cir.setReturnValue(seasonal);
    }

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

    private static float getBlendFactor(Season season) {
        return switch (season) {
            case SPRING -> 0.60f;
            case SUMMER -> 0.40f;
            case AUTUMN -> 0.80f;
            case WINTER -> 0.88f;
        };
    }
}
