package com.customseasons.handler;

import com.customseasons.season.SeasonManager;
import net.minecraft.server.level.ServerLevel;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.tick.ServerTickEvent;

@EventBusSubscriber(modid = "customseasons", bus = EventBusSubscriber.Bus.GAME)
public class SeasonTickHandler {

    @SubscribeEvent
    public static void onServerTick(ServerTickEvent.Post event) {
        ServerLevel overworld = event.getServer().overworld();
        SeasonManager.tick(overworld);
    }
}
