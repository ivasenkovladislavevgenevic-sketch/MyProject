package com.customseasons.mixin;

import com.customseasons.color.SeasonColors;
import com.customseasons.network.ClientSeasonHolder;
import com.customseasons.season.SeasonType;
import net.minecraft.world.level.GrassColor;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/**
 * Overrides vanilla grass color based on the current season.
 */
@Mixin(GrassColor.class)
public class GrassColorMixin {

    @Inject(method = "get(DD)I", at = @At("HEAD"), cancellable = true)
    private static void customseasons_onGet(double temperature, double humidity,
                                            CallbackInfoReturnable<Integer> cir) {
        SeasonType season = ClientSeasonHolder.getCurrentSeason();
        if (season != null && season != SeasonType.SUMMER) {
            cir.setReturnValue(SeasonColors.getGrassColor(season));
        }
    }
}
