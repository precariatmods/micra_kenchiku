import random
from mctools import RCONClient
import time

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")

def cmd(command):
    print(command)
    print(mcr.command(command))

# --------------------
# 木を1本作る
# --------------------
def tree(x0, y0, z0):

    height = random.randint(4, 8)

    # 幹
    for y in range(y0, y0 + height):
        cmd(f"setblock {x0} {y} {z0} minecraft:oak_log")

    top = y0 + height - 1

    # 葉っぱ 下段
    for x in range(x0 - 2, x0 + 3):
        for z in range(z0 - 2, z0 + 3):
            cmd(f"setblock {x} {top} {z} minecraft:oak_leaves")

    # 葉っぱ 中段
    for x in range(x0 - 2, x0 + 3):
        for z in range(z0 - 2, z0 + 3):
            cmd(f"setblock {x} {top + 1} {z} minecraft:oak_leaves")

    # 葉っぱ 上段
    for x in range(x0 - 1, x0 + 2):
        for z in range(z0 - 1, z0 + 2):
            cmd(f"setblock {x} {top + 2} {z} minecraft:oak_leaves")

    # 頂上
    cmd(f"setblock {x0} {top + 3} {z0} minecraft:oak_leaves")


for i in range(10):
    cmd (f"fill {-20} {1} {-20} {20} {15} {20} air")
    # --------------------
    # 中央の木
    # --------------------
    tree(0, 1, 0)
    # --------------------
    # 周囲8本
    # 位置を少しランダムにする
    # --------------------
    for base_x in [-10, 0, 10]:
        for base_z in [-10, 0, 10]:
            # 中央はすでに作ったので除外
            if base_x == 0 and base_z == 0:
                continue
            x = base_x + random.randint(-3, 3)
            z = base_z + random.randint(-3, 3)
            tree(x, 1, z)
    time.sleep(1)