package com.seasonalworld.mod.network;

import com.seasonalworld.mod.SeasonalWorldMod;
import com.seasonalworld.mod.client.SeasonColorClient;
import com.seasonalworld.mod.season.Season;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.ResourceLocation;
import net.neoforged.neoforge.network.handling.IPayloadContext;

/**
 * Packet sent from server → client to sync the current season.
 * Sent on login and whenever season changes.
 */
public record SeasonSyncPacket(Season season) implements CustomPacketPayload {

    public static final ResourceLocation ID_RL = ResourceLocation.fromNamespaceAndPath(
            SeasonalWorldMod.MOD_ID, "season_sync");
    public static final CustomPacketPayload.Type<SeasonSyncPacket> TYPE =
            new CustomPacketPayload.Type<>(ID_RL);

    public static final StreamCodec<FriendlyByteBuf, SeasonSyncPacket> STREAM_CODEC =
            StreamCodec.of(
                    (buf, pkt) -> buf.writeEnum(pkt.season),
                    buf -> new SeasonSyncPacket(buf.readEnum(Season.class))
            );

    @Override
    public Type<? extends CustomPacketPayload> type() {
        return TYPE;
    }

    /** Called on the client when the packet is received. */
    public static void handleClient(SeasonSyncPacket packet, IPayloadContext ctx) {
        ctx.enqueueWork(() -> {
            SeasonColorClient.setCurrentSeason(packet.season());
            SeasonalWorldMod.LOGGER.info("[SeasonalWorld] Client received season: {}", packet.season());
        });
    }
}
