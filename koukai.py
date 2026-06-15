import time
from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")


def cmd(command):
    print(command)
    print(mcr.command(command))

def block(x, y, z, b):
    cmd(f"setblock {x} {y} {z} {b}")

def rect(x1, y1, z1, x2, y2, z2, b):
    cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {b}")
# 大阪市中央公会堂 風
# 表面だけ版
# cmd("...") が使える前提です

# --------------------
# ブロック指定
# --------------------
STONE = "minecraft:smooth_stone"
STONE_BRICK = "minecraft:stone_bricks"
STONE_SLAB = "minecraft:stone_brick_slab"
BRICK = "minecraft:bricks"
WHITE = "minecraft:white_concrete"
GREEN = "minecraft:dark_prismarine"
GLASS = "minecraft:glass_pane"
DOOR = "minecraft:dark_oak_door"
QUARTZ = "minecraft:quartz_pillar"
LANTERN = "minecraft:lantern"
GOLD = "minecraft:gold_block"
AIR = "minecraft:air"

Z = 0


def setb(x, y, z, block):
    cmd(f"setblock {x} {y} {z} {block}")


def fill(x1, y1, z1, x2, y2, z2, block):
    cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}")


# --------------------
# 一度、建築範囲を消す
# --------------------
fill(-45, 1, -3, 45, 50, 3, AIR)

# --------------------
# 地面・階段
# --------------------
fill(-42, 0, -6, 42, 0, 6, STONE_BRICK)

for i in range(6):
    fill(-24 - i, 1 + i, -6 - i, 24 + i, 1 + i, -6 - i, STONE_BRICK)

# # --------------------
# # 赤レンガ壁
# # --------------------
# # 中央
# fill(-22, 7, Z, 22, 26, Z, BRICK)

# # 左右塔
# fill(-38, 5, Z, -24, 32, Z, BRICK)
# fill(24, 5, Z, 38, 32, Z, BRICK)

# # 左右端の低い壁
# fill(-44, 4, Z, -39, 20, Z, BRICK)
# fill(39, 4, Z, 44, 20, Z, BRICK)

# --------------------
# 赤レンガ壁 強化版
# --------------------

# 中央下部：白壁を減らして赤レンガを広くする
fill(-22, 7, Z, 22, 26, Z, BRICK)

# 中央の白い柱間だけ石にする
for x in [-18, -9, 0, 9, 18]:
    fill(x, 7, Z - 1, x, 24, Z - 1, WHITE)

# 入口まわりだけ白石
for x in [-10, 0, 10]:
    fill(x - 3, 7, Z - 2, x + 3, 15, Z - 2, WHITE)
    fill(x - 2, 7, Z - 3, x + 2, 12, Z - 3, DOOR)

# 左右塔：全面赤レンガを強める
fill(-38, 5, Z, -24, 32, Z, BRICK)
fill(24, 5, Z, 38, 32, Z, BRICK)

# 左右端の赤レンガ面も広げる
fill(-44, 4, Z, -39, 22, Z, BRICK)
fill(39, 4, Z, 44, 22, Z, BRICK)

# 白い縦ラインは細めに
for x in [-44, -38, -24, -22, 22, 24, 38, 44]:
    fill(x, 4, Z - 1, x, 28, Z - 1, STONE)

# 水平ラインも控えめ
for y in [6, 24, 32]:
    fill(-44, y, Z - 1, 44, y, Z - 1, STONE)

# --------------------
# 白・石の縦ライン
# --------------------
for x in [-44, -39, -38, -24, -22, 22, 24, 38, 39, 44]:
    fill(x, 4, Z - 1, x, 28, Z - 1, STONE)

# 中央の白壁部分
fill(-18, 7, Z - 1, 18, 24, Z - 1, WHITE)

# 赤レンガを中央白壁に戻す
for x in [-14, -7, 0, 7, 14]:
    fill(x - 2, 9, Z - 2, x + 2, 21, Z - 2, BRICK)

# 水平ライン
for y in [5, 6, 7, 24, 27, 32]:
    fill(-44, y, Z - 1, 44, y, Z - 1, STONE)

# 塔の下部白ライン
for y in [8, 10, 12]:
    fill(-44, y, Z - 2, -24, y, Z - 2, WHITE)
    fill(24, y, Z - 2, 44, y, Z - 2, WHITE)

# --------------------
# 中央の柱
# --------------------
for x in [-16, -8, 0, 8, 16]:
    fill(x, 7, Z - 3, x, 23, Z - 3, QUARTZ)
    setb(x, 24, Z - 3, STONE)
    setb(x, 6, Z - 3, STONE)

# 柱上の横梁
fill(-22, 24, Z - 3, 22, 26, Z - 3, STONE)

# --------------------
# 中央入口 3つ
# --------------------
for x in [-10, 0, 10]:
    fill(x - 2, 7, Z - 4, x + 2, 12, Z - 4, DOOR)
    fill(x - 3, 13, Z - 4, x + 3, 14, Z - 4, STONE)
    fill(x - 3, 15, Z - 4, x + 3, 15, Z - 4, GREEN)
    setb(x, 16, Z - 4, LANTERN)

# --------------------
# 中央窓
# --------------------
for x in [-14, -7, 0, 7, 14]:
    fill(x - 2, 16, Z - 4, x + 2, 22, Z - 4, GLASS)
    fill(x - 3, 15, Z - 4, x + 3, 15, Z - 4, STONE)
    fill(x - 3, 23, Z - 4, x + 3, 23, Z - 4, STONE)
    fill(x - 3, 16, Z - 4, x - 3, 22, Z - 4, STONE)
    fill(x + 3, 16, Z - 4, x + 3, 22, Z - 4, STONE)

# --------------------
# 左右塔の大窓
# --------------------
for x in [-31, 31]:
    fill(x - 3, 13, Z - 3, x + 3, 21, Z - 3, GLASS)
    fill(x - 4, 12, Z - 3, x + 4, 12, Z - 3, STONE)
    fill(x - 4, 22, Z - 3, x + 4, 22, Z - 3, STONE)
    fill(x - 4, 13, Z - 3, x - 4, 21, Z - 3, STONE)
    fill(x + 4, 13, Z - 3, x + 4, 21, Z - 3, STONE)

# --------------------
# 左右塔の丸窓
# --------------------
for x in [-31, 31]:
    # 丸窓の白枠
    setb(x, 27, Z - 4, GLASS)
    setb(x - 1, 27, Z - 4, GLASS)
    setb(x + 1, 27, Z - 4, GLASS)
    setb(x, 26, Z - 4, GLASS)
    setb(x, 28, Z - 4, GLASS)

    setb(x - 2, 27, Z - 4, WHITE)
    setb(x + 2, 27, Z - 4, WHITE)
    setb(x, 25, Z - 4, WHITE)
    setb(x, 29, Z - 4, WHITE)

    setb(x - 1, 25, Z - 4, STONE)
    setb(x + 1, 25, Z - 4, STONE)
    setb(x - 1, 29, Z - 4, STONE)
    setb(x + 1, 29, Z - 4, STONE)

# --------------------
# 中央アーチ窓
# --------------------
# 半円のガラス
for y in range(27, 42):
    dy = y - 27
    half = int((16 * 16 - dy * dy) ** 0.5)
    fill(-half, y, Z - 5, half, y, Z - 5, GLASS)

# アーチの縦格子
for x in range(-15, 16, 3):
    fill(x, 27, Z - 6, x, 41, Z - 6, STONE)

# アーチの横格子
for y in range(28, 41, 3):
    dy = y - 27
    half = int((16 * 16 - dy * dy) ** 0.5)
    fill(-half, y, Z - 6, half, y, Z - 6, STONE)

# 赤白アーチ模様
for i, x in enumerate(range(-18, 19, 3)):
    block = WHITE if i % 2 == 0 else BRICK
    fill(x, 27, Z - 7, x + 1, 42, Z - 7, block)

# 緑の大アーチ屋根
for y in range(40, 47):
    dy = y - 40
    half = int((22 * 22 - dy * dy) ** 0.5)
    fill(-half, y, Z - 8, half, y, Z - 8, GREEN)

# 中央屋根の厚み
fill(-20, 43, Z - 7, 20, 45, Z - 7, GREEN)
fill(-16, 46, Z - 7, 16, 46, Z - 7, GREEN)

# --------------------
# 左右塔の屋根
# --------------------
for cx in [-31, 31]:
    # 塔上部の白い箱
    fill(cx - 6, 33, Z - 1, cx + 6, 38, Z - 1, STONE)
    fill(cx - 4, 34, Z - 2, cx + 4, 38, Z - 2, WHITE)

    # 上部窓
    fill(cx - 2, 34, Z - 3, cx + 2, 38, Z - 3, GLASS)
    fill(cx - 3, 34, Z - 3, cx - 3, 38, Z - 3, STONE)
    fill(cx + 3, 34, Z - 3, cx + 3, 38, Z - 3, STONE)

    # ドーム
    for y in range(39, 46):
        dy = y - 39
        half = int((7 * 7 - dy * dy) ** 0.5)
        fill(cx - half, y, Z - 4, cx + half, y, Z - 4, GREEN)

    # 尖塔
    fill(cx, 46, Z - 4, cx, 51, Z - 4, GOLD)
    setb(cx, 52, Z - 4, LANTERN)

# --------------------
# 左右の低い緑屋根
# --------------------
for cx in [-42, 42]:
    for y in range(21, 28):
        dy = y - 21
        half = max(1, int((8 * 8 - dy * dy) ** 0.5))
        fill(cx - half, y, Z - 3, cx + half, y, Z - 3, GREEN)

# --------------------
# 小さい庇・装飾
# --------------------
for x in [-31, 31]:
    # 下窓の三角屋根風
    fill(x - 4, 11, Z - 4, x + 4, 11, Z - 4, STONE)
    fill(x - 3, 12, Z - 4, x + 3, 12, Z - 4, STONE)
    fill(x - 2, 13, Z - 4, x + 2, 13, Z - 4, STONE)
    setb(x, 14, Z - 4, STONE)

for x in [-35, 35]:
    setb(x, 5, Z - 4, LANTERN)
    setb(x, 6, Z - 4, LANTERN)

# --------------------
# 手前の街灯
# --------------------
for x in [-36, 36]:
    fill(x, 1, -6, x, 8, -6, STONE)
    setb(x, 9, -6, LANTERN)
    setb(x - 1, 8, -6, LANTERN)
    setb(x + 1, 8, -6, LANTERN)

print("大阪市中央公会堂 風 表面建築 完了")