package com.customseasons;

import com.customseasons.network.ClientSeasonHolder;
import com.customseasons.network.SeasonSyncPacket;
import com.customseasons.season.SeasonManager;
import com.customseasons.season.SeasonType;
import com.mojang.brigadier.arguments.StringArgumentType;
import net.minecraft.commands.Commands;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.Mod;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.event.RegisterCommandsEvent;
import net.neoforged.neoforge.event.entity.player.PlayerEvent;
import net.neoforged.neoforge.network.event.RegisterPayloadHandlersEvent;
import net.neoforged.neoforge.network.registration.PayloadRegistrar;

@Mod("customseasons")
public class CustomSeasonsMod {

    public CustomSeasonsMod(IEventBus modBus) {
        // Register network payloads
        modBus.addListener(this::onRegisterPayloads);

        // Register game events
        NeoForge.EVENT_BUS.addListener(this::onRegisterCommands);
        NeoForge.EVENT_BUS.addListener(this::onPlayerLogin);
    }

    private void onRegisterPayloads(RegisterPayloadHandlersEvent event) {
        PayloadRegistrar registrar = event.registrar("1");
        registrar.playToClient(
                SeasonSyncPacket.TYPE,
                SeasonSyncPacket.CODEC,
                (packet, ctx) -> {
                    // Client-side handler
                    ctx.enqueueWork(() -> ClientSeasonHolder.setCurrentSeason(packet.season()));
                }
        );
    }

    private void onRegisterCommands(RegisterCommandsEvent event) {
        event.getDispatcher().register(
                Commands.literal("season")
                        .requires(src -> src.hasPermission(2))
                        .then(Commands.literal("get")
                                .executes(ctx -> {
                                    ServerLevel overworld = ctx.getSource().getServer().overworld();
                                    SeasonType season = SeasonManager.getSeason(overworld);
                                    ctx.getSource().sendSuccess(
                                            () -> Component.translatable("commands.customseasons.season.get",
                                                    Component.translatable(season.getTranslationKey())),
                                            false
                                    );
                                    return 1;
                                })
                        )
                        .then(Commands.literal("set")
                                .then(Commands.argument("season", StringArgumentType.word())
                                        .suggests((ctx, builder) -> {
                                            for (SeasonType s : SeasonType.values()) {
                                                builder.suggest(s.name().toLowerCase());
                                            }
                                            return builder.buildFuture();
                                        })
                                        .executes(ctx -> {
                                            String arg = StringArgumentType.getString(ctx, "season").toUpperCase();
                                            SeasonType season;
                                            try {
                                                season = SeasonType.valueOf(arg);
                                            } catch (IllegalArgumentException e) {
                                                ctx.getSource().sendFailure(
                                                        Component.literal("Unknown season: " + arg)
                                                );
                                                return 0;
                                            }
                                            ServerLevel overworld = ctx.getSource().getServer().overworld();
                                            SeasonManager.setSeason(overworld, season);
                                            ctx.getSource().sendSuccess(
                                                    () -> Component.translatable("commands.customseasons.season.set",
                                                            Component.translatable(season.getTranslationKey())),
                                                    true
                                            );
                                            return 1;
                                        })
                                )
                        )
        );
    }

    private void onPlayerLogin(PlayerEvent.PlayerLoggedInEvent event) {
        if (event.getEntity().level() instanceof ServerLevel level
                && level.dimension().equals(net.minecraft.world.level.Level.OVERWORLD)) {
            SeasonType season = SeasonManager.getSeason(level);
            SeasonSyncPacket packet = new SeasonSyncPacket(season);
            net.neoforged.neoforge.network.PacketDistributor.sendToPlayer(
                    (net.minecraft.server.level.ServerPlayer) event.getEntity(), packet
            );
        }
    }
}
