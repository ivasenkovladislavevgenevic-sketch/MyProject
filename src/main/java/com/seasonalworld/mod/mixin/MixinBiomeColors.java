package com.seasonalworld.mod.mixin;

import com.seasonalworld.mod.client.SeasonColorClient;
import com.seasonalworld.mod.season.BiomeChecker;
import com.seasonalworld.mod.season.Season;
import net.minecraft.client.renderer.BiomeColors;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.BlockAndTintGetter;
import net.minecraft.world.level.ColorResolver;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/**
 * Per-block biome color override — checks biome before applying seasonal tint.
 * Desert biomes are excluded from seasonal color changes.
 */
@Mixin(BiomeColors.class)
public class MixinBiomeColors {

    @Inject(
        method = "getAverageFoliageColor(Lnet/minecraft/world/level/BlockAndTintGetter;Lnet/minecraft/core/BlockPos;)I",
        at = @At("RETURN"),
        cancellable = true
    )
    private static void checkDesertFoliage(BlockAndTintGetter level, BlockPos pos,
                                            CallbackInfoReturnable<Integer> cir) {
        // Skip seasonal color for desert biomes
        if (level instanceof net.minecraft.world.level.LevelReader reader) {
            var biomeHolder = reader.getBiome(pos);
            if (BiomeChecker.isDesertBiome(biomeHolder)) return;
        }
        // Seasonal color already applied by MixinFoliageColor; nothing extra here
    }

    @Inject(
        method = "getAverageGrassColor(Lnet/minecraft/world/level/BlockAndTintGetter;Lnet/minecraft/core/BlockPos;)I",
        at = @At("RETURN"),
        cancellable = true
    )
    private static void checkDesertGrass(BlockAndTintGetter level, BlockPos pos,
                                          CallbackInfoReturnable<Integer> cir) {
        if (level instanceof net.minecraft.world.level.LevelReader reader) {
            var biomeHolder = reader.getBiome(pos);
            if (BiomeChecker.isDesertBiome(biomeHolder)) return;
        }
    }
}
