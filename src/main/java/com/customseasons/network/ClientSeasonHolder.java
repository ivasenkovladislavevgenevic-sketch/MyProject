package com.customseasons.network;

import com.customseasons.season.SeasonType;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.api.distmarker.OnlyIn;

@OnlyIn(Dist.CLIENT)
public class ClientSeasonHolder {

    private static SeasonType currentSeason = SeasonType.SUMMER;

    public static SeasonType getCurrentSeason() {
        return currentSeason;
    }

    public static void setCurrentSeason(SeasonType season) {
        currentSeason = season;
        // Invalidate chunk rendering caches so foliage colors update immediately
        net.minecraft.client.Minecraft.getInstance().levelRenderer.allChanged();
    }
}
