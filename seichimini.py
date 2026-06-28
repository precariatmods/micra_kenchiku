from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")
cmd = f"fill {-20} {1} {-20} {20} {15} {20} air"
mcr.command(cmd)



cmd = f"fill {-0} {1} {-30} {0} {15} {0} air"
mcr.command(cmd)

cmd = f"fill {0} {1} {0} {30} {15} {30} air"
mcr.command(cmd)


# cmd = f"fill {-20} {0} {-20} {20} {0} {20} minecraft:sea_lantern"

cmd = f"fill {-20} {0} {-20} {20} {0} {20} minecraft:stone"
mcr.command(cmd)

