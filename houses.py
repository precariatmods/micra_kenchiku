from mctools import RCONClient
import time

HOST = "192.168.1.10"
PORT = 25575
PASSWORD = "pass"

BASE_X = 0
BASE_Y = 0
BASE_Z = 0

def cmd(mcr, c):
    print(c)
    mcr.command(c)
    time.sleep(0.02)

# ------------------------------------------------------------
# 家を1軒作る関数
# x0, y0, z0 が家の左前座標
# 家サイズ：10×10
# ------------------------------------------------------------

def make_house(mcr, x0, y0, z0):
    # 地面 10×10
    cmd(mcr, f"fill {x0} {y0} {z0} {x0+9} {y0} {z0+9} minecraft:oak_planks")

    # 壁 高さ4
    cmd(mcr, f"fill {x0} {y0+1} {z0} {x0+9} {y0+4} {z0} minecraft:oak_log")
    cmd(mcr, f"fill {x0} {y0+1} {z0+9} {x0+9} {y0+4} {z0+9} minecraft:oak_log")
    cmd(mcr, f"fill {x0} {y0+1} {z0} {x0} {y0+4} {z0+9} minecraft:oak_log")
    cmd(mcr, f"fill {x0+9} {y0+1} {z0} {x0+9} {y0+4} {z0+9} minecraft:oak_log")

    # 中を空洞に
    cmd(mcr, f"fill {x0+1} {y0+1} {z0+1} {x0+8} {y0+4} {z0+8} minecraft:air")

    # ドア
    cmd(mcr, f"setblock {x0+4} {y0+1} {z0} minecraft:air")
    cmd(mcr, f"setblock {x0+4} {y0+2} {z0} minecraft:air")
    cmd(mcr, f"setblock {x0+5} {y0+1} {z0} minecraft:air")
    cmd(mcr, f"setblock {x0+5} {y0+2} {z0} minecraft:air")

    # 窓
    cmd(mcr, f"fill {x0+2} {y0+2} {z0} {x0+3} {y0+3} {z0} minecraft:glass_pane")
    cmd(mcr, f"fill {x0+6} {y0+2} {z0} {x0+7} {y0+3} {z0} minecraft:glass_pane")

    # 斜め屋根
    # Z方向に長い屋根。左右から中央へ上がる形
    for i in range(5):
        left_x = x0 - 1 + i
        right_x = x0 + 10 - i
        y = y0 + 5 + i

        cmd(mcr, f"fill {left_x} {y} {z0-1} {left_x} {y} {z0+10} minecraft:dark_oak_stairs[facing=east]")
        cmd(mcr, f"fill {right_x} {y} {z0-1} {right_x} {y} {z0+10} minecraft:dark_oak_stairs[facing=west]")

    # 屋根のてっぺん
    cmd(mcr, f"fill {x0+4} {y0+10} {z0-1} {x0+5} {y0+10} {z0+10} minecraft:dark_oak_planks")


# ------------------------------------------------------------
# 石畳の通路
# ------------------------------------------------------------

def make_paths(mcr, y0):
    # 全体の地面
    cmd(mcr, f"fill -40 {y0} -40 49 {y0} 49 minecraft:grass_block")

    # 中央の十字通路
    cmd(mcr, f"fill -40 {y0} 4 49 {y0} 6 minecraft:cobblestone")
    cmd(mcr, f"fill 4 {y0} -40 6 {y0} 49 minecraft:cobblestone")

    # 家と家の間の通路
    # 家の間隔は18、家サイズ10なので、隙間に通路を通す
    for x in [-22, -4, 14, 32]:
        cmd(mcr, f"fill {x} {y0} -40 {x+2} {y0} 49 minecraft:cobblestone")

    for z in [-22, -4, 14, 32]:
        cmd(mcr, f"fill -40 {y0} {z} 49 {y0} {z+2} minecraft:cobblestone")


# ------------------------------------------------------------
# 村を作る
# 1 + 8 + 16 = 25軒
# ------------------------------------------------------------

def make_village(mcr):
    y0 = BASE_Y
    # 家の配置
    # 5×5 に配置すると、
    # 中央1軒、周囲8軒、外周16軒になる
    #
    # 家サイズ 10
    # 間隔 18
    # つまり家と家の間に8ブロックほど隙間ができる

    spacing = 18
    start_x = BASE_X - spacing * 2
    start_z = BASE_Z - spacing * 2

    # 1周目：中央1軒
    make_house(mcr, BASE_X, y0, BASE_Z)
    time.sleep(0.5)

    # 2周目：周囲8軒
    for gx in range(-1, 2):
        for gz in range(-1, 2):
            if gx == 0 and gz == 0:
                continue

            x0 = BASE_X + gx * spacing
            z0 = BASE_Z + gz * spacing
            make_house(mcr, x0, y0, z0)

    time.sleep(0.5)

    # 3周目：外周16軒
    for gx in range(-2, 3):
        for gz in range(-2, 3):
            if abs(gx) != 2 and abs(gz) != 2:
                continue

            x0 = BASE_X + gx * spacing
            z0 = BASE_Z + gz * spacing
            make_house(mcr, x0, y0, z0)

    # 最後に通路をもう一度上書き
    # 家の床は残しつつ、家の隙間だけ石畳が目立つ
    make_paths(mcr, y0)

    # 中央広場
    cmd(mcr, f"fill -3 {y0} -3 13 {y0} 13 minecraft:stone_bricks")
    cmd(mcr, f"fill 3 {y0+1} 3 7 {y0+1} 7 minecraft:water")

    # 広場の明かり
    for x, z in [(-4, -4), (14, -4), (-4, 14), (14, 14)]:
        cmd(mcr, f"fill {x} {y0+1} {z} {x} {y0+4} {z} minecraft:oak_fence")
        cmd(mcr, f"setblock {x} {y0+5} {z} minecraft:glowstone")




    # 撮影位置
    cmd(mcr, "tp @p 60 45 -70 40 25")

    print("25軒の村を作りました")


# ------------------------------------------------------------
# 実行
# ------------------------------------------------------------

with RCONClient(HOST, port=PORT) as mcr:
    mcr.login(PASSWORD)
    make_village(mcr)