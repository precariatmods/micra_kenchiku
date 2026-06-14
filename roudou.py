# ============================================================
# 労働センター風
# 外観 + 1F内部（柱・梁・天井・配管）
# ============================================================

import time
from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")

def cmd(command):
    print(command)
    print(mcr.command(command))

# ------------------------------------------------------------
# 補助関数
# ------------------------------------------------------------

def fill(x1, y1, z1, x2, y2, z2, block):
    cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}")


def setblock(x, y, z, block):
    cmd(f"setblock {x} {y} {z} {block}")


# ------------------------------------------------------------
# 全体設定
# ------------------------------------------------------------

# 建物サイズ
X_MIN = -60
X_MAX = 60
Z_MIN = -35
Z_MAX = 35

Y_FLOOR = 1
Y_1F_CEIL = 12
Y_2F = 16
Y_3F = 24
Y_4F = 32
Y_TOP = 40

WALL = "minecraft:smooth_stone"
CONCRETE = "minecraft:light_gray_concrete"
DARK = "minecraft:gray_concrete"
GLASS = "minecraft:light_blue_stained_glass_pane"
FLOOR = "minecraft:green_terracotta"
PIPE = "minecraft:cut_copper"
DARK_PIPE = "minecraft:weathered_copper"
LIGHT = "minecraft:sea_lantern"
BLACK = "minecraft:black_concrete"
WHITE = "minecraft:white_concrete"
SIGN = "minecraft:white_wool"


# ------------------------------------------------------------
# 0. 整地
# ------------------------------------------------------------

def clear_area():
    print("整地中...")
    fill(-75, 0, -50, 75, 55, 50, "minecraft:air")
    fill(-75, 0, -50, 75, 0, 50, "minecraft:sea_lantern")
    time.sleep(1)


# ------------------------------------------------------------
# 1. 外観を作る
# ------------------------------------------------------------

def build_exterior():
    print("外観を作成中...")

    # 1F床
    fill(X_MIN, Y_FLOOR, Z_MIN, X_MAX, Y_FLOOR, Z_MAX, FLOOR)

    # 1F天井・2F床
    fill(X_MIN, Y_1F_CEIL, Z_MIN, X_MAX, Y_1F_CEIL, Z_MAX, CONCRETE)

    # 2F・3F・4Fの床
    fill(X_MIN, Y_2F, Z_MIN, X_MAX, Y_2F, Z_MAX, CONCRETE)
    fill(X_MIN, Y_3F, Z_MIN, X_MAX, Y_3F, Z_MAX, CONCRETE)
    fill(X_MIN, Y_4F, Z_MIN, X_MAX, Y_4F, Z_MAX, CONCRETE)

    # 屋上
    fill(X_MIN, Y_TOP, Z_MIN, X_MAX, Y_TOP, Z_MAX, DARK)

    # 外壁：左右
    fill(X_MIN, Y_2F, Z_MIN, X_MIN, Y_TOP, Z_MAX, WALL)
    fill(X_MAX, Y_2F, Z_MIN, X_MAX, Y_TOP, Z_MAX, WALL)

    # 外壁：背面
    fill(X_MIN, Y_2F, Z_MAX, X_MAX, Y_TOP, Z_MAX, WALL)

    # 正面外壁は窓を多めにする
    z = Z_MIN

    # 2F正面
    fill(X_MIN, Y_2F, z, X_MAX, Y_3F, z, WALL)
    for x in range(X_MIN + 5, X_MAX - 5, 10):
        fill(x, Y_2F + 2, z, x + 5, Y_3F - 2, z, GLASS)

    # 3F正面
    fill(X_MIN, Y_3F, z, X_MAX, Y_4F, z, WALL)
    for x in range(X_MIN + 5, X_MAX - 5, 8):
        fill(x, Y_3F + 2, z, x + 4, Y_4F - 2, z, GLASS)

    # 4F正面
    fill(X_MIN, Y_4F, z, X_MAX, Y_TOP, z, DARK)
    for x in range(X_MIN + 5, X_MAX - 5, 8):
        fill(x, Y_4F + 2, z, x + 4, Y_TOP - 2, z, GLASS)

    # 1F正面の柱と開口部
    for x in range(X_MIN + 10, X_MAX, 15):
        fill(x - 1, Y_FLOOR, Z_MIN, x + 1, Y_1F_CEIL, Z_MIN + 2, WALL)

    # 正面ひさし
    fill(X_MIN - 2, Y_1F_CEIL + 1, Z_MIN - 3, X_MAX + 2, Y_1F_CEIL + 2, Z_MIN + 8, CONCRETE)

    # 屋上の上部機械室風
    fill(-45, Y_TOP + 1, -25, -25, Y_TOP + 8, -5, DARK)
    fill(20, Y_TOP + 1, -25, 45, Y_TOP + 6, -5, DARK)

    # 正面上部の看板
    fill(-25, Y_TOP + 1, Z_MIN - 1, 25, Y_TOP + 3, Z_MIN - 1, WHITE)
    fill(-22, Y_TOP + 2, Z_MIN - 2, 22, Y_TOP + 2, Z_MIN - 2, BLACK)

    # 入口横断幕風
    fill(-35, Y_1F_CEIL - 2, Z_MIN - 2, 35, Y_1F_CEIL - 1, Z_MIN - 2, SIGN)

    time.sleep(1)


# ------------------------------------------------------------
# 2. 1F内部の柱
# ------------------------------------------------------------

def build_inside_columns():
    print("1F内部の柱を作成中...")

    # 太い柱をグリッド配置
    for x in range(X_MIN + 12, X_MAX - 5, 12):
        for z in range(Z_MIN + 8, Z_MAX - 5, 10):

            # 3x3の太い柱
            fill(x - 1, Y_FLOOR + 1, z - 1,
                 x + 1, Y_1F_CEIL - 1, z + 1,
                 WALL)

            # 柱の根元を少し暗くする
            fill(x - 2, Y_FLOOR + 1, z - 2,
                 x + 2, Y_FLOOR + 1, z + 2,
                 DARK)

    time.sleep(1)


# ------------------------------------------------------------
# 3. 天井梁
# ------------------------------------------------------------

def build_ceiling_beams():
    print("天井梁を作成中...")

    y = Y_1F_CEIL - 1

    # 横方向の梁
    for z in range(Z_MIN + 5, Z_MAX - 3, 10):
        fill(X_MIN, y, z - 1, X_MAX, y + 1, z + 1, DARK)

    # 奥行方向の梁
    for x in range(X_MIN + 6, X_MAX - 3, 12):
        fill(x - 1, y, Z_MIN, x + 1, y + 1, Z_MAX, DARK)

    # 天井面を少し水色っぽくする
    for x in range(X_MIN, X_MAX + 1, 12):
        for z in range(Z_MIN, Z_MAX + 1, 10):
            fill(x, Y_1F_CEIL, z, min(x + 8, X_MAX), Y_1F_CEIL, min(z + 6, Z_MAX),
                 "minecraft:light_blue_concrete")

    time.sleep(1)


# ------------------------------------------------------------
# 4. 配管・照明
# ------------------------------------------------------------

def build_pipes_and_lights():
    print("配管と照明を作成中...")

    # 横方向の太い配管
    for z in range(Z_MIN + 6, Z_MAX - 2, 10):
        fill(X_MIN + 5, Y_1F_CEIL - 3, z, X_MAX - 5, Y_1F_CEIL - 3, z, PIPE)

    # 奥行方向の配管
    for x in range(X_MIN + 8, X_MAX - 5, 16):
        fill(x, Y_1F_CEIL - 4, Z_MIN + 5, x, Y_1F_CEIL - 4, Z_MAX - 5, DARK_PIPE)

    # 吊り下げ棒
    for x in range(X_MIN + 10, X_MAX - 5, 16):
        for z in range(Z_MIN + 8, Z_MAX - 5, 12):
            fill(x, Y_1F_CEIL - 1, z, x, Y_1F_CEIL - 4, z, "minecraft:iron_bars")

    # 蛍光灯風
    for x in range(X_MIN + 8, X_MAX - 8, 16):
        for z in range(Z_MIN + 6, Z_MAX - 6, 14):
            fill(x - 2, Y_1F_CEIL - 2, z, x + 2, Y_1F_CEIL - 2, z, LIGHT)

    time.sleep(1)


# ------------------------------------------------------------
# 5. 入口・シャッター・小物
# ------------------------------------------------------------

def build_entrance_details():
    print("入口まわりを作成中...")

    z = Z_MIN - 1

    # シャッター風
    fill(-25, Y_FLOOR + 1, z, -12, Y_FLOOR + 8, z, "minecraft:iron_block")
    for y in range(Y_FLOOR + 2, Y_FLOOR + 8, 2):
        fill(-25, y, z - 1, -12, y, z - 1, "minecraft:gray_concrete")

    fill(12, Y_FLOOR + 1, z, 25, Y_FLOOR + 8, z, "minecraft:iron_block")
    for y in range(Y_FLOOR + 2, Y_FLOOR + 8, 2):
        fill(12, y, z - 1, 25, y, z - 1, "minecraft:gray_concrete")

    # 掲示板風
    fill(-50, Y_FLOOR + 2, z, -44, Y_FLOOR + 6, z, "minecraft:white_concrete")
    fill(44, Y_FLOOR + 2, z, 50, Y_FLOOR + 6, z, "minecraft:white_concrete")

    # ゴミ箱・ベンチ風
    fill(-40, Y_FLOOR + 1, Z_MIN + 5, -38, Y_FLOOR + 3, Z_MIN + 7, "minecraft:cauldron")
    fill(30, Y_FLOOR + 1, Z_MIN + 10, 38, Y_FLOOR + 1, Z_MIN + 11, "minecraft:dark_oak_planks")

    # 木を少し
    for x in [-45, 45]:
        fill(x, Y_FLOOR + 1, Z_MIN - 8, x, Y_FLOOR + 6, Z_MIN - 8, "minecraft:dark_oak_log")
        fill(x - 3, Y_FLOOR + 6, Z_MIN - 11, x + 3, Y_FLOOR + 10, Z_MIN - 5, "minecraft:oak_leaves")

    time.sleep(1)


# ------------------------------------------------------------
# 実行
# ------------------------------------------------------------

clear_area()
build_exterior()
build_inside_columns()
build_ceiling_beams()
build_pipes_and_lights()
build_entrance_details()

print("労働センター風建築 完成")