package com.seasonalworld.mod.mixin;

import com.seasonalworld.mod.SeasonalWorldMod;
import com.seasonalworld.mod.client.SeasonColorClient;
import com.seasonalworld.mod.season.Season;
import net.minecraft.client.renderer.LevelRenderer;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Hooks into LevelRenderer to trigger chunk re-renders when season changes,
 * so foliage colors update without requiring a manual F3+A.
 */
@Mixin(LevelRenderer.class)
public class MixinLevelRenderer {

    private Season lastKnownSeason = null;

    @Inject(method = "renderLevel", at = @At("HEAD"))
    private void checkSeasonChange(CallbackInfo ci) {
        Season current = SeasonColorClient.getCurrentSeason();
        if (current != lastKnownSeason) {
            lastKnownSeason = current;
            // Reload chunk colors
            LevelRenderer self = (LevelRenderer) (Object) this;
            self.allChanged();
            SeasonalWorldMod.LOGGER.info("[SeasonalWorld] Client season changed to {}, reloading chunk colors.", current);
        }
    }
}
