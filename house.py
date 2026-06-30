from mctools import RCONClient
import time


mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")

BASE_X = 0
BASE_Y = 0
BASE_Z = 0

def cmd(mcr, c):
    mcr.command(c)
    time.sleep(0.02)

with RCONClient("192.168.1.10", port=25575) as mcr:
    mcr.login("サーバーで設定したRCONパスワード")

    x0 = BASE_X
    y0 = BASE_Y
    z0 = BASE_Z

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

    print("斜め屋根の家を作りました")