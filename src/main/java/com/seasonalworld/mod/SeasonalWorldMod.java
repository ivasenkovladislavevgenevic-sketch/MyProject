package com.seasonalworld.mod;

import com.mojang.logging.LogUtils;
import com.seasonalworld.mod.config.SeasonConfig;
import com.seasonalworld.mod.network.SeasonSyncPacket;
import com.seasonalworld.mod.season.SeasonManager;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.ModContainer;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.config.ModConfig;
import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;
import net.neoforged.neoforge.network.event.RegisterPayloadHandlersEvent;
import net.neoforged.neoforge.network.registration.PayloadRegistrar;
import org.slf4j.Logger;

@Mod(SeasonalWorldMod.MOD_ID)
public class SeasonalWorldMod {

    public static final String MOD_ID = "seasonalworld";
    public static final Logger LOGGER = LogUtils.getLogger();

    public SeasonalWorldMod(IEventBus modEventBus, ModContainer modContainer) {
        modEventBus.addListener(this::commonSetup);
        modEventBus.addListener(this::registerPayloads);
        modContainer.registerConfig(ModConfig.Type.COMMON, SeasonConfig.SPEC);
        LOGGER.info("[SeasonalWorld] Mod initialized.");
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        LOGGER.info("[SeasonalWorld] Common setup complete. Seasons active.");
        SeasonManager.init();
    }

    private void registerPayloads(final RegisterPayloadHandlersEvent event) {
        PayloadRegistrar registrar = event.registrar("1");
        registrar.playToClient(
                SeasonSyncPacket.TYPE,
                SeasonSyncPacket.STREAM_CODEC,
                SeasonSyncPacket::handleClient
        );
    }
}
