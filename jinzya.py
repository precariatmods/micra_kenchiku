from mctools import RCONClient
import math
import time

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")

def block(x, y, z, b):
    mcr.command(f"setblock {x} {y} {z} {b}")

def fill(x1, y1, z1, x2, y2, z2, b):
    mcr.command(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {b}")

# ===== 参道 =====
fill(-3, 1, -80, 3, 1, 25, "minecraft:smooth_stone")
fill(-5, 1, -80, -4, 1, 25, "minecraft:stone_bricks")
fill(4, 1, -80, 5, 1, 25, "minecraft:stone_bricks")

# ===== 鳥居 =====
red = "minecraft:red_concrete"
black = "minecraft:blackstone"

# 柱
fill(-12, 1, -55, -9, 18, -55, red)
fill(9, 1, -55, 12, 18, -55, red)

# 笠木・貫
fill(-18, 18, -55, 18, 20, -55, red)
fill(-22, 21, -55, 22, 22, -55, black)
fill(-15, 13, -55, 15, 14, -55, red)

# 中央額
fill(-2, 15, -56, 2, 18, -56, "minecraft:gold_block")

# ===== 拝殿の基壇 =====
fill(-32, 1, 25, 32, 3, 65, "minecraft:stone_bricks")
fill(-28, 4, 29, 28, 4, 61, "minecraft:smooth_stone")

# ===== 本体床・壁 =====
fill(-25, 5, 32, 25, 18, 58, "minecraft:white_concrete")

# 正面を少し開ける
fill(-18, 6, 31, 18, 15, 31, "minecraft:air")

# 赤い柱
pillar_positions = [-24, -12, 0, 12, 24]
for x in pillar_positions:
    fill(x, 5, 30, x+2, 19, 32, red)
    fill(x, 5, 58, x+2, 19, 60, red)

for z in [34, 46, 58]:
    fill(-26, 5, z, -24, 19, z+2, red)
    fill(24, 5, z, 26, 19, z+2, red)

# 梁
fill(-28, 18, 30, 28, 20, 32, red)
fill(-28, 18, 58, 28, 20, 60, red)
fill(-28, 18, 30, -26, 20, 60, red)
fill(26, 18, 30, 28, 20, 60, red)

# 黒い格子窓
for x in [-18, -10, 10, 18]:
    fill(x, 8, 30, x+4, 15, 30, "minecraft:black_stained_glass_pane")

# ===== 大屋根 =====
roof = "minecraft:dark_prismarine"
edge = "minecraft:dark_prismarine_slab"

# 反りのある屋根：横に広く、上に行くほど狭くする
for i in range(0, 12):
    y = 20 + i // 2
    x1 = -40 + i
    x2 = 40 - i
    z1 = 22 + i
    z2 = 68 - i

    fill(x1, y, z1, x2, y, z2, roof)

# 軒を強調
fill(-44, 20, 20, 44, 20, 24, edge)
fill(-44, 20, 66, 44, 20, 70, edge)
fill(-44, 20, 20, -40, 20, 70, edge)
fill(40, 20, 20, 44, 20, 70, edge)

# 屋根中央の棟
fill(-6, 27, 39, 6, 29, 51, black)
fill(-3, 30, 42, 3, 31, 48, "minecraft:gold_block")

# ===== 千木っぽい飾り =====
for i in range(0, 8):
    block(-8-i, 29+i, 44, black)
    block(8+i, 29+i, 44, black)
    block(-8-i, 29+i, 48, black)
    block(8+i, 29+i, 48, black)

# ===== 灯籠 =====
for x in [-10, 10]:
    for z in [-35, -15, 5, 20]:
        fill(x, 1, z, x, 3, z, "minecraft:stone_bricks")
        block(x, 4, z, "minecraft:sea_lantern")
        block(x, 5, z, "minecraft:stone_brick_slab")

# ===== しめ縄風 =====
fill(-8, 16, 30, 8, 16, 30, "minecraft:oak_fence")
for x in [-6, 0, 6]:
    fill(x, 14, 30, x, 16, 30, "minecraft:white_wool")

print("神社っぽい建築 完了")