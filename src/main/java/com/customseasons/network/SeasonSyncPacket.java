package com.customseasons.network;

import com.customseasons.season.SeasonType;
import io.netty.buffer.ByteBuf;
import net.minecraft.network.codec.ByteBufCodecs;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.ResourceLocation;

public record SeasonSyncPacket(SeasonType season) implements CustomPacketPayload {

    public static final Type<SeasonSyncPacket> TYPE =
            new Type<>(ResourceLocation.fromNamespaceAndPath("customseasons", "season_sync"));

    public static final StreamCodec<ByteBuf, SeasonSyncPacket> CODEC = StreamCodec.composite(
            ByteBufCodecs.INT.map(SeasonType::fromId, SeasonType::ordinal),
            SeasonSyncPacket::season,
            SeasonSyncPacket::new
    );

    @Override
    public Type<? extends CustomPacketPayload> type() {
        return TYPE;
    }
}
