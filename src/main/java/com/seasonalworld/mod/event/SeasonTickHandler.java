package com.seasonalworld.mod.event;

import com.seasonalworld.mod.SeasonalWorldMod;
import com.seasonalworld.mod.season.Season;
import com.seasonalworld.mod.season.SeasonManager;
import net.minecraft.server.level.ServerLevel;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.tick.LevelTickEvent;

/**
 * Ticks the SeasonManager every server tick.
 */
@EventBusSubscriber(modid = SeasonalWorldMod.MOD_ID, bus = EventBusSubscriber.Bus.GAME)
public class SeasonTickHandler {

    @SubscribeEvent
    public static void onLevelTick(LevelTickEvent.Post event) {
        if (!(event.getLevel() instanceof ServerLevel level)) return;
        if (level.isClientSide()) return;
        // Only tick the overworld to avoid multiple season timers
        if (!level.dimension().equals(net.minecraft.world.level.Level.OVERWORLD)) return;

        SeasonManager.onServerTick(level);
    }
}
