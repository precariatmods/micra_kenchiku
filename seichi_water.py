from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")


for i in range(0, 50, 1):
    cmd = f"fill {100} {i} {100} {200} {i+1} {200} water"
    mcr.command(cmd)
    cmd = f"fill {100} {i} {0} {200} {i+1} {100} water"
    mcr.command(cmd)
    cmd = f"fill {100} {i} {-100} {200} {i+1} {0} water"
    mcr.command(cmd)
    cmd = f"fill {100} {i} {-200} {200} {i+1} {-100} awaterir"
    mcr.command(cmd)

for i in range(0, 50, 1):
    cmd = f"fill {0} {i} {100} {100} {i+1} {200} water"
    mcr.command(cmd)
    cmd = f"fill {0} {i} {0} {100} {i+1} {100} water"
    mcr.command(cmd)
    cmd = f"fill {0} {i} {-100} {100} {i+1} {0} water"
    mcr.command(cmd)
    cmd = f"fill {0} {i} {-200} {100} {i+1} {-100} water"
    mcr.command(cmd)

for i in range(0, 50, 1):
    cmd = f"fill {-100} {i} {100} {0} {i+1} {200} water"
    mcr.command(cmd)
    cmd = f"fill {-100} {i} {0} {0} {i+1} {100} water"
    mcr.command(cmd)
    cmd = f"fill {-100} {i} {-100} {0} {i+1} {0} water"
    mcr.command(cmd)
    cmd = f"fill {-100} {i} {-200} {0} {i+1} {-100} water"
    mcr.command(cmd)

for i in range(0, 50, 1):
    cmd = f"fill {-200} {i} {100} {-100} {i+1} {200} water"
    mcr.command(cmd)
    cmd = f"fill {-200} {i} {0} {-100} {i+1} {100} water"
    mcr.command(cmd)
    cmd = f"fill {-200} {i} {-100} {-100} {i+1} {0} water"
    mcr.command(cmd)
    cmd = f"fill {-200} {i} {-200} {-100} {i+1} {-100} water"
    mcr.command(cmd)

for x in range(-200, 200, 100):
    for z in range(-200, 200, 100):

        x2 = min(x + 99, 200)
        z2 = min(z + 99, 200)

        cmd = (
            f"fill {x} -2 {z} "
            f"{x2} 0 {z2} "
            f"minecraft:sea_lantern"
        )
        mcr.command(cmd)
