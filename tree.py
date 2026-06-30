from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")

def cmd(command):
    print(command)
    print(mcr.command(command))


# --------------------
# 木を1本作る
# --------------------

x0 = 0
y0 = 1
z0 = 0

# 幹
for y in range(y0, y0 + 6):
    cmd(f"setblock {x0} {y} {z0} minecraft:oak_log")

# 葉っぱ 下段
for x in range(x0 - 2, x0 + 3):
    for z in range(z0 - 2, z0 + 3):
        cmd(f"setblock {x} {y0 + 4} {z} minecraft:oak_leaves")

# 葉っぱ 中段
for x in range(x0 - 2, x0 + 3):
    for z in range(z0 - 2, z0 + 3):
        cmd(f"setblock {x} {y0 + 5} {z} minecraft:oak_leaves")

# 葉っぱ 上段
for x in range(x0 - 1, x0 + 2):
    for z in range(z0 - 1, z0 + 2):
        cmd(f"setblock {x} {y0 + 6} {z} minecraft:oak_leaves")
# 一番上
cmd(f"setblock {x0} {y0 + 7} {z0} minecraft:oak_leaves")
