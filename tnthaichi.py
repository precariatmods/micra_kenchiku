from mctools import RCONClient
import time
mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")
def cmd(command):
    print(command)
    print(mcr.command(command))
# TNT設置条件
x = 338
y = 109
z_start = 150
z_end = -50
interval = 2
# Z方向にTNTを設置
for z in range(z_start, z_end - 1, -interval):
    cmd(f"setblock {x} {y} {z} tnt")
    time.sleep(0.05)
cmd(f"setblock {x} {y} {z_end} tnt")
# TNT設置条件
x = x
y = y+1
z_start = z_start-1
z_end = -50
interval = 2
# Z方向にTNTを設置
for z in range(z_start, z_end - 1, -interval):
    cmd(f"setblock {x} {y} {z} tnt")
    time.sleep(0.05)
cmd(f"setblock {x} {y} {z_end} tnt")
# TNT設置条件
x = x
y = y+1
z_start = z_start-1
z_end = -50
interval = 2
# Z方向にTNTを設置
for z in range(z_start, z_end - 1, -interval):
    cmd(f"setblock {x} {y} {z} tnt")
    time.sleep(0.05)
cmd(f"setblock {x} {y} {z_end} tnt")