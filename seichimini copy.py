from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")



cmd = f"fill {-50} {1} {0} {50} {150} {1} air"
mcr.command(cmd)

