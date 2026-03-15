package com.seasonalworld.mod.event;

import com.seasonalworld.mod.SeasonalWorldMod;
import com.seasonalworld.mod.network.SeasonSyncPacket;
import com.seasonalworld.mod.season.Season;
import com.seasonalworld.mod.season.SeasonManager;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.event.entity.player.PlayerEvent;
import net.neoforged.neoforge.network.PacketDistributor;

/**
 * Sends season sync packets to players on join and on season change.
 */
@EventBusSubscriber(modid = SeasonalWorldMod.MOD_ID, bus = EventBusSubscriber.Bus.GAME)
public class SeasonNetworkHandler {

    private static Season lastBroadcastSeason = null;

    /** Send current season when a player logs in. */
    @SubscribeEvent
    public static void onPlayerJoin(PlayerEvent.PlayerLoggedInEvent event) {
        if (!(event.getEntity() instanceof ServerPlayer player)) return;
        ServerLevel level = (ServerLevel) player.level();
        Season season = SeasonManager.getCurrentSeason(level);
        PacketDistributor.sendToPlayer(player, new SeasonSyncPacket(season));
    }

    /** Broadcast season to all players when it changes (called from SeasonTickHandler). */
    public static void broadcastSeasonChange(Season season) {
        if (season == lastBroadcastSeason) return;
        lastBroadcastSeason = season;
        PacketDistributor.sendToAllPlayers(new SeasonSyncPacket(season));
    }
}
