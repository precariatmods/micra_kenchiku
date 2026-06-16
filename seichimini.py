from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")
cmd = f"fill {-20} {1} {-20} {20} {15} {20} air"
mcr.command(cmd)