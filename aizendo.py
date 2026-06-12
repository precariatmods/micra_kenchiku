import time
from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")

CX = 0
CY = 0
CZ = 0

def cmd(command):
    print(command)
    print(mcr.command(command))
    time.sleep(0.05)

# いったん周辺を少し消す
cmd("fill -15 0 -15 15 25 15 minecraft:air")

# 地面
cmd("fill -15 -1 -15 15 -1 15 minecraft:grass_block")

# 基壇 下段 21×21
cmd("fill -10 0 -10 10 0 10 minecraft:stone_bricks")

# 基壇 中段 17×17
cmd("fill -8 1 -8 8 1 8 minecraft:stone_bricks")

# 木の床 13×13
cmd("fill -6 2 -6 6 2 6 minecraft:dark_oak_planks")

# 正面階段 Zマイナス方向
cmd("fill -3 0 -13 3 0 -11 minecraft:stone_brick_stairs[facing=north]")
cmd("fill -3 1 -10 3 1 -9 minecraft:stone_brick_stairs[facing=north]")
cmd("fill -3 2 -8 3 2 -7 minecraft:stone_brick_stairs[facing=north]")

# 柵っぽい外周
cmd("fill -10 1 -10 10 1 -10 minecraft:dark_oak_fence")
cmd("fill -10 1 10 10 1 10 minecraft:dark_oak_fence")
cmd("fill -10 1 -10 -10 1 10 minecraft:dark_oak_fence")
cmd("fill 10 1 -10 10 1 10 minecraft:dark_oak_fence")

# 正面階段部分だけ柵を空ける
cmd("fill -3 1 -10 3 1 -10 minecraft:air")

# 柱位置確認用
for x, z in [
    (-6, -6), (0, -6), (6, -6),
    (-6,  0),          (6,  0),
    (-6,  6), (0,  6), (6,  6),
]:
    cmd(f"fill {x} 3 {z} {x} 8 {z} minecraft:dark_oak_log")

print("Phase1 土台 完了")


# --------------------------------
# Phase2 壁・欄干・扉
# --------------------------------

# =====================
# 柱
# =====================

for x, z in [
    (-6,-6),(0,-6),(6,-6),
    (-6, 0),       (6, 0),
    (-6, 6),(0, 6),(6, 6)
]:
    cmd(
        f"fill {x} 3 {z} {x} 10 {z} minecraft:dark_oak_log"
    )

# =====================
# 欄干
# =====================

cmd("fill -6 3 -6 6 3 -6 minecraft:dark_oak_fence")
cmd("fill -6 3  6 6 3  6 minecraft:dark_oak_fence")

cmd("fill -6 3 -6 -6 3 6 minecraft:dark_oak_fence")
cmd("fill  6 3 -6  6 3 6 minecraft:dark_oak_fence")

# 正面中央を空ける
cmd("fill -1 3 -6 1 3 -6 minecraft:air")

# =====================
# 壁
# =====================

# 左
cmd(
    "fill -5 4 -5 -5 8 5 minecraft:stripped_dark_oak_wood"
)

# 右
cmd(
    "fill 5 4 -5 5 8 5 minecraft:stripped_dark_oak_wood"
)

# 奥
cmd(
    "fill -5 4 5 5 8 5 minecraft:stripped_dark_oak_wood"
)

# =====================
# 正面
# =====================

# 左壁
cmd(
    "fill -5 4 -5 -2 8 -5 minecraft:stripped_dark_oak_wood"
)

# 右壁
cmd(
    "fill 2 4 -5 5 8 -5 minecraft:stripped_dark_oak_wood"
)

# =====================
# 扉
# =====================

cmd(
    "fill -1 4 -5 1 8 -5 minecraft:air"
)

cmd(
    "setblock 0 4 -5 minecraft:dark_oak_door"
)

# =====================
# 上部梁
# =====================

cmd(
    "fill -6 10 -6 6 10 -6 minecraft:dark_oak_log"
)

cmd(
    "fill -6 10 6 6 10 6 minecraft:dark_oak_log"
)

cmd(
    "fill -6 10 -6 -6 10 6 minecraft:dark_oak_log"
)

cmd(
    "fill 6 10 -6 6 10 6 minecraft:dark_oak_log"
)

print("Phase2 完了")


# =====================
# 屋根の芯
# =====================

# 建物本体の上に黒っぽい屋根を載せる
cmd("fill -7 11 -7 7 11 7 minecraft:dark_oak_planks")

# 1段目：大きく張り出す
cmd("fill -9 10 -9 9 10 9 minecraft:dark_oak_slab[type=top]")

# 2段目：さらに張り出す
cmd("fill -10 9 -10 10 9 10 minecraft:dark_oak_slab[type=top]")

# 3段目：最大張り出し
cmd("fill -11 8 -11 11 8 11 minecraft:dark_oak_slab[type=top]")

# 中を少し空けて、厚ぼったさを減らす
cmd("fill -8 9 -8 8 10 8 minecraft:air")

# =====================
# 中央の屋根上台座
# =====================

cmd("fill -5 12 -5 5 12 5 minecraft:smooth_stone")
cmd("fill -4 13 -4 4 13 4 minecraft:smooth_stone")

# =====================
# 屋根の反り表現
# 四隅だけ少し上げる
# =====================

for x, z in [
    (-11, -11),
    (-11,  11),
    ( 11, -11),
    ( 11,  11),
]:
    cmd(f"setblock {x} 9 {z} minecraft:dark_oak_slab[type=top]")
    cmd(f"setblock {x} 10 {z} minecraft:dark_oak_fence")

# =====================
# 軒先の飾り
# =====================

cmd("fill -11 8 -11 11 8 -11 minecraft:dark_oak_stairs[facing=north]")
cmd("fill -11 8 11 11 8 11 minecraft:dark_oak_stairs[facing=south]")
cmd("fill -11 8 -11 -11 8 11 minecraft:dark_oak_stairs[facing=west]")
cmd("fill 11 8 -11 11 8 11 minecraft:dark_oak_stairs[facing=east]")

# =====================
# 屋根裏の梁
# =====================

cmd("fill -8 9 -8 8 9 -8 minecraft:dark_oak_log")
cmd("fill -8 9 8 8 9 8 minecraft:dark_oak_log")
cmd("fill -8 9 -8 -8 9 8 minecraft:dark_oak_log")
cmd("fill 8 9 -8 8 9 8 minecraft:dark_oak_log")

print("Phase3 下屋根 完了")
# --------------------------------
# Phase4 多宝塔の丸い胴
# --------------------------------



# =====================
# 丸胴の床
# =====================

# 下屋根中央の上に円形っぽい台を作る
for x in range(-4, 5):
    for z in range(-4, 5):
        d2 = x*x + z*z
        if d2 <= 16:
            cmd(f"setblock {x} 14 {z} minecraft:smooth_stone")

# =====================
# 丸胴の壁
# =====================

# 円周だけ白い壁を立てる
for y in range(15, 19):
    for x in range(-4, 5):
        for z in range(-4, 5):
            d2 = x*x + z*z

            # 半径3.2〜4.2くらいを壁にする
            if 10 <= d2 <= 17:
                cmd(f"setblock {x} {y} {z} minecraft:white_terracotta")

# =====================
# 中を空洞にする
# =====================

for y in range(15, 19):
    for x in range(-2, 3):
        for z in range(-2, 3):
            cmd(f"setblock {x} {y} {z} minecraft:air")

# =====================
# 正面だけ入口風に空ける
# Zマイナス方向
# =====================

for y in range(15, 18):
    for x in range(-1, 2):
        cmd(f"setblock {x} {y} -4 minecraft:air")

# =====================
# 丸胴の柱っぽい縦線
# =====================

for x, z in [
    (0, -4),
    (3, -3),
    (4, 0),
    (3, 3),
    (0, 4),
    (-3, 3),
    (-4, 0),
    (-3, -3),
]:
    cmd(f"fill {x} 15 {z} {x} 19 {z} minecraft:dark_oak_log")

# =====================
# 上下の帯
# =====================

# 下帯
for x in range(-4, 5):
    for z in range(-4, 5):
        d2 = x*x + z*z
        if 10 <= d2 <= 17:
            cmd(f"setblock {x} 15 {z} minecraft:dark_oak_planks")

# 上帯
for x in range(-4, 5):
    for z in range(-4, 5):
        d2 = x*x + z*z
        if 10 <= d2 <= 17:
            cmd(f"setblock {x} 19 {z} minecraft:dark_oak_planks")

# =====================
# 2階を載せるための正方形台
# =====================

cmd("fill -4 20 -4 4 20 4 minecraft:smooth_stone")

print("Phase4 丸い胴 完了")

# --------------------------------
# Phase5 2階部分
# --------------------------------

# =====================
# 2階床
# =====================

cmd("fill -4 21 -4 4 21 4 minecraft:dark_oak_planks")

# =====================
# 2階柱
# =====================

for x, z in [
    (-4,-4), (0,-4), (4,-4),
    (-4, 0),          (4, 0),
    (-4, 4), (0, 4), (4, 4),
]:
    cmd(f"fill {x} 22 {z} {x} 27 {z} minecraft:dark_oak_log")

# =====================
# 2階壁
# =====================

# 正面は中央を空ける
cmd("fill -4 22 -4 -2 26 -4 minecraft:white_terracotta")
cmd("fill  2 22 -4  4 26 -4 minecraft:white_terracotta")

# 左右と奥
cmd("fill -4 22 4 4 26 4 minecraft:white_terracotta")
cmd("fill -4 22 -4 -4 26 4 minecraft:white_terracotta")
cmd("fill 4 22 -4 4 26 4 minecraft:white_terracotta")

# 正面中央の開口
cmd("fill -1 22 -4 1 25 -4 minecraft:air")

# =====================
# 窓っぽい黒い部分
# =====================

cmd("fill -1 23 4 1 24 4 minecraft:black_stained_glass")
cmd("fill -4 23 -1 -4 24 1 minecraft:black_stained_glass")
cmd("fill 4 23 -1 4 24 1 minecraft:black_stained_glass")

# =====================
# 2階の欄干
# =====================

cmd("fill -5 22 -5 5 22 -5 minecraft:dark_oak_fence")
cmd("fill -5 22  5 5 22  5 minecraft:dark_oak_fence")
cmd("fill -5 22 -5 -5 22 5 minecraft:dark_oak_fence")
cmd("fill  5 22 -5  5 22 5 minecraft:dark_oak_fence")

# 正面中央を空ける
cmd("fill -1 22 -5 1 22 -5 minecraft:air")

# =====================
# 上部梁
# =====================

cmd("fill -4 27 -4 4 27 -4 minecraft:dark_oak_log")
cmd("fill -4 27  4 4 27  4 minecraft:dark_oak_log")
cmd("fill -4 27 -4 -4 27 4 minecraft:dark_oak_log")
cmd("fill  4 27 -4  4 27 4 minecraft:dark_oak_log")

print("Phase5 2階部分 完了")
# --------------------------------
# Phase6 上屋根
# --------------------------------

import time

def cmd(command):
    print(command)
    print(mcr.command(command))
    time.sleep(0.05)

# =====================
# 上屋根の芯
# =====================

cmd("fill -5 28 -5 5 28 5 minecraft:dark_oak_planks")

# 1段目
cmd("fill -6 27 -6 6 27 6 minecraft:dark_oak_slab[type=top]")

# 2段目
cmd("fill -7 26 -7 7 26 7 minecraft:dark_oak_slab[type=top]")

# 3段目 最大張り出し
cmd("fill -8 25 -8 8 25 8 minecraft:dark_oak_slab[type=top]")

# 中央を空けて厚みを調整
cmd("fill -5 26 -5 5 27 5 minecraft:air")

# =====================
# 軒先
# =====================

cmd("fill -8 25 -8 8 25 -8 minecraft:dark_oak_stairs[facing=north]")
cmd("fill -8 25 8 8 25 8 minecraft:dark_oak_stairs[facing=south]")
cmd("fill -8 25 -8 -8 25 8 minecraft:dark_oak_stairs[facing=west]")
cmd("fill 8 25 -8 8 25 8 minecraft:dark_oak_stairs[facing=east]")

# =====================
# 反り表現：四隅を少し上げる
# =====================

for x, z in [
    (-8, -8),
    (-8,  8),
    ( 8, -8),
    ( 8,  8),
]:
    cmd(f"setblock {x} 26 {z} minecraft:dark_oak_slab[type=top]")
    cmd(f"setblock {x} 27 {z} minecraft:dark_oak_fence")

# =====================
# 屋根上の小さい台座
# =====================

cmd("fill -3 29 -3 3 29 3 minecraft:smooth_stone")
cmd("fill -2 30 -2 2 30 2 minecraft:smooth_stone")

print("Phase6 上屋根 完了")
# --------------------------------
# Phase6 上屋根
# --------------------------------

import time

def cmd(command):
    print(command)
    print(mcr.command(command))
    time.sleep(0.05)

# =====================
# 上屋根の芯
# =====================

cmd("fill -5 28 -5 5 28 5 minecraft:dark_oak_planks")

# 1段目
cmd("fill -6 27 -6 6 27 6 minecraft:dark_oak_slab[type=top]")

# 2段目
cmd("fill -7 26 -7 7 26 7 minecraft:dark_oak_slab[type=top]")

# 3段目 最大張り出し
cmd("fill -8 25 -8 8 25 8 minecraft:dark_oak_slab[type=top]")

# 中央を空けて厚みを調整
cmd("fill -5 26 -5 5 27 5 minecraft:air")

# =====================
# 軒先
# =====================

cmd("fill -8 25 -8 8 25 -8 minecraft:dark_oak_stairs[facing=north]")
cmd("fill -8 25 8 8 25 8 minecraft:dark_oak_stairs[facing=south]")
cmd("fill -8 25 -8 -8 25 8 minecraft:dark_oak_stairs[facing=west]")
cmd("fill 8 25 -8 8 25 8 minecraft:dark_oak_stairs[facing=east]")

# =====================
# 反り表現：四隅を少し上げる
# =====================

for x, z in [
    (-8, -8),
    (-8,  8),
    ( 8, -8),
    ( 8,  8),
]:
    cmd(f"setblock {x} 26 {z} minecraft:dark_oak_slab[type=top]")
    cmd(f"setblock {x} 27 {z} minecraft:dark_oak_fence")

# =====================
# 屋根上の小さい台座
# =====================

cmd("fill -3 29 -3 3 29 3 minecraft:smooth_stone")
cmd("fill -2 30 -2 2 30 2 minecraft:smooth_stone")

print("Phase6 上屋根 完了")
import time

def cmd(command):
    print(command)
    print(mcr.command(command))
    time.sleep(0.05)

# 芯棒
cmd("fill 0 31 0 0 48 0 minecraft:lightning_rod")

# --------------------
# 九輪
# --------------------

for y in [33,35,37,39,41,43,45]:

    # 東西
    cmd(f"fill -1 {y} 0 1 {y} 0 minecraft:gold_block")

    # 南北
    cmd(f"fill 0 {y} -1 0 {y} 1 minecraft:gold_block")

# --------------------
# 伏鉢
# --------------------

cmd("fill -2 31 -2 2 31 2 minecraft:cut_copper")
cmd("fill -1 32 -1 1 32 1 minecraft:cut_copper")

# --------------------
# 宝珠
# --------------------

cmd("setblock 0 47 0 minecraft:gold_block")
cmd("setblock 0 48 0 minecraft:gold_block")
cmd("setblock 0 49 0 minecraft:lightning_rod")

print("相輪完成")

# --------------------------------
# 相輪から四隅へ鎖
# --------------------------------

TOP_Y = 55

for i in range(11):

    x = i
    y = TOP_Y - i * 2
    z = i

    # 北東
    cmd(
        f"setblock {x} {y} {z} minecraft:iron_bars"
    )

    # 北西
    cmd(
        f"setblock {-x} {y} {z} minecraft:iron_bars"
    )

    # 南東
    cmd(
        f"setblock {x} {y} {-z} minecraft:iron_bars"
    )

    # 南西
    cmd(
        f"setblock {-x} {y} {-z} minecraft:iron_bars"
    )

# --------------------------------
# 鎖の先端にランタン
# --------------------------------

cmd("setblock 10 35 10 minecraft:lantern")
cmd("setblock -10 35 10 minecraft:lantern")
cmd("setblock 10 35 -10 minecraft:lantern")
cmd("setblock -10 35 -10 minecraft:lantern")

print("鎖 完成")