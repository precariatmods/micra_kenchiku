from mctools import RCONClient
import time

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")

def cmd(command):
    print(command)
    print(mcr.command(command))


wall = "oak_planks"
glass = "glass"
air = "air"


def make_house(x0, y0, z0, width, depth, height):
    # 正面の壁
    cmd(f"fill {x0} {y0 + 1} {z0} {x0 + width - 1} {y0 + height} {z0} {wall}")

    # 背面の壁
    cmd(f"fill {x0} {y0 + 1} {z0 + depth - 1} {x0 + width - 1} {y0 + height} {z0 + depth - 1} {wall}")

    # 左の壁
    cmd(f"fill {x0} {y0 + 1} {z0} {x0} {y0 + height} {z0 + depth - 1} {wall}")

    # 右の壁
    cmd(f"fill {x0 + width - 1} {y0 + 1} {z0} {x0 + width - 1} {y0 + height} {z0 + depth - 1} {wall}")

    # 屋根
    cmd(f"fill {x0} {y0 + height + 1} {z0} {x0 + width - 1} {y0 + height + 1} {z0 + depth - 1} {wall}")

    # 扉
    door_x = x0 + width // 2

    cmd(f"setblock {door_x} {y0 + 1} {z0} {air}")
    cmd(f"setblock {door_x} {y0 + 2} {z0} {air}")

    cmd(f"setblock {door_x} {y0 + 1} {z0} minecraft:oak_door[half=lower,facing=south,hinge=left,open=false,powered=false]")
    cmd(f"setblock {door_x} {y0 + 2} {z0} minecraft:oak_door[half=upper,facing=south,hinge=left,open=false,powered=false]")

    # 窓
    cmd(f"setblock {x0 + 1} {y0 + 3} {z0} {glass}")
    cmd(f"setblock {x0 + width - 2} {y0 + 3} {z0} {glass}")


y0 = 0
z0 = 0
for i in range(1,10):
    # 左：小さい家
    make_house(
        x0=i,
        y0=y0,
        z0=z0,
        width=5,
        depth=5,
        height=4
    )
    time.sleep(1)
    cmd(f"fill {-20} {1} {-20} {20} {15} {20} air")