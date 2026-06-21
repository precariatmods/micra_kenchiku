

from mctools import RCONClient
import time
mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")

def cmd(command):
    print(command)
    print(mcr.command(command))

x0 = 0
y0 = 0
z0 = 0

width = 7
depth = 7
height = 5

wall = "oak_planks"
glass = "glass"
air = "air"
water = "water"
# わかりやすさ優先で　絶対座標を書く

# 正面の壁 Z方向固定 ①
cmd(f"fill {0} { 1} {0} {x0 + width - 1} {y0 + height} {z0} {wall}")

# 背面の壁 z=方向固定（奥行き分①のz座標を足す）　0 + 7 = 7
cmd(f"fill {0} { 1} {z0 + depth - 1} {x0 + width - 1} {y0 + height} {z0 + depth - 1} {wall}")

# 左の壁　X座標固定　x=0　　②
cmd(f"fill {0} { 1} {z0} {0} {y0 + height} {z0 + depth - 1} {wall}")

# 右の壁 x=width-1
cmd(f"fill {x0 + width - 1} {y0 + 1} {z0} {x0 + width - 1} {y0 + height} {z0 + depth - 1} {wall}")

# 扉の穴
door_x = x0 + width // 2
cmd(f"setblock {door_x} {y0 + 1} {z0} {air}")
cmd(f"setblock {door_x} {y0 + 2} {z0} {air}")

cmd(f"setblock {door_x} {y0 + 1} {z0} minecraft:oak_door[half=lower,facing=south,hinge=left,open=false,powered=false]")
cmd(f"setblock {door_x} {y0 + 2} {z0} minecraft:oak_door[half=upper,facing=south,hinge=left,open=false,powered=false]")

time.sleep(1)
#溝をつくる
# 家のまわりに2マス深い溝を作る
moat_top = y0
moat_bottom = y0 - 1

# 前
cmd(f"fill {x0 - 1} {moat_bottom} {z0 - 1} {x0 + width} {moat_top} {z0 - 1} {air}")
cmd(f"fill {x0 - 1} {moat_bottom} {z0 - 1} {x0 + width} {moat_bottom} {z0 - 1} {water}")

# 後ろ
cmd(f"fill {x0 - 1} {moat_bottom} {z0 + depth} {x0 + width} {moat_top} {z0 + depth} {air}")
cmd(f"fill {x0 - 1} {moat_bottom} {z0 + depth} {x0 + width} {moat_bottom} {z0 + depth} {water}")

# 左
cmd(f"fill {x0 - 1} {moat_bottom} {z0 - 1} {x0 - 1} {moat_top} {z0 + depth} {air}")
cmd(f"fill {x0 - 1} {moat_bottom} {z0 - 1} {x0 - 1} {moat_bottom} {z0 + depth} {water}")

# 右
cmd(f"fill {x0 + width} {moat_bottom} {z0 - 1} {x0 + width} {moat_top} {z0 + depth} {air}")
# 窓
cmd(f"setblock {x0 + 1} {y0 + 3} {z0} {glass}")