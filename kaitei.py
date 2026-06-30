from mctools import RCONClient
import time

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")


def cmd(command):
    print(command)
    print(mcr.command(command))


# fill上限対策用
# Minecraftのfillは一度に大量ブロックを置けないので分割する
CHUNK_X = 32
CHUNK_Y = 16
CHUNK_Z = 32


def chunked_fill(x1, y1, z1, x2, y2, z2, block, delay=0.02):
    x_min, x_max = sorted([x1, x2])
    y_min, y_max = sorted([y1, y2])
    z_min, z_max = sorted([z1, z2])

    for xs in range(x_min, x_max + 1, CHUNK_X):
        xe = min(xs + CHUNK_X - 1, x_max)

        for ys in range(y_min, y_max + 1, CHUNK_Y):
            ye = min(ys + CHUNK_Y - 1, y_max)

            for zs in range(z_min, z_max + 1, CHUNK_Z):
                ze = min(zs + CHUNK_Z - 1, z_max)

                command = f"fill {xs} {ys} {zs} {xe} {ye} {ze} {block}"
                cmd(command)
                time.sleep(delay)


# ==================================================
# 1. プラスマイナス200四方、高さ50まで水にする
# ==================================================

chunked_fill(
    -200, 0, -200,
     200, 50, 200,
    "minecraft:water"
)




# ==================================================
# 2. プラスマイナス50、高さ30のガラス外殻を作る
# ==================================================

glass = "minecraft:glass"

# 床
chunked_fill(-50, 0, -50, 50, 0, 50, glass)

# 天井
chunked_fill(-50, 30, -50, 50, 30, 50, glass)

# 北側の壁
chunked_fill(-50, 0, -50, 50, 30, -50, glass)

# 南側の壁
chunked_fill(-50, 0, 50, 50, 30, 50, glass)

# 西側の壁
chunked_fill(-50, 0, -50, -50, 30, 50, glass)

# 東側の壁
chunked_fill(50, 0, -50, 50, 30, 50, glass)



# ==================================================
# 3. 内部を空気にする
#    x,zは±49、高さは1〜29
# ==================================================

chunked_fill(
    -49, 1, -49,
     49, 29, 49,
    "minecraft:air"
)