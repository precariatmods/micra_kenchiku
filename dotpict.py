from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("pass")

PIXEL = 2
BASE_X = 0
BASE_Y = 1
BASE_Z = 0

data = [
".R........R.",
".RR......RR.",
"..YY....YY..",
".YYYY..YYYY.",
".YYYYYYYYYY.",
"..YYYYYYYY..",
"...YYYYYY...",
"....RRRR....",
"...RRRRRR...",
"..RRYYRR...",
".YRYYYYRY..",
".YYYYYYYY..",
"..RR..RR...",
"..RR..RR...",
".BB....BB..",
".BB....BB..",
]

colors = {
    "R": "minecraft:red_wool",
    "Y": "minecraft:yellow_wool",
    "B": "minecraft:brown_wool",
}

height = len(data)

for row, line in enumerate(data):

    y = BASE_Y + (height - row - 1) * PIXEL

    for col, ch in enumerate(line):

        if ch == ".":
            continue

        x = BASE_X + col * PIXEL

        block = colors[ch]

        cmd = (
            f"fill "
            f"{x} {y} {BASE_Z} "
            f"{x+PIXEL-1} {y+PIXEL-1} {BASE_Z} "
            f"{block}"
        )

        mcr.command(cmd)

print("ばんざいドット絵完成")