import time
from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")


def cmd(command):
    print(command)
    print(mcr.command(command))
    time.sleep(0.01)


def fill(x1, y1, z1, x2, y2, z2, block):
    cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}")


def setblock(x, y, z, block):
    cmd(f"setblock {x} {y} {z} {block}")


x0 = 0
y0 = 0
z0 = 0

air = "minecraft:air"
ground = "minecraft:grass_block"
rail = "minecraft:iron_block"
sleeper = "minecraft:dark_oak_planks"
wheel = "minecraft:black_concrete"
body = "minecraft:red_concrete"
body_dark = "minecraft:gray_concrete"
roof = "minecraft:blackstone"
glass = "minecraft:light_blue_stained_glass"
light = "minecraft:sea_lantern"
trim = "minecraft:yellow_concrete"
metal = "minecraft:iron_block"
smoke = "minecraft:light_gray_wool"
platform = "minecraft:smooth_stone"


# clear space
fill(x0 - 60, y0, z0 - 6, x0 + 160, y0 + 18, z0 + 18, air)

# ground
fill(x0 - 60, y0, z0 - 6, x0 + 160, y0, z0 + 18, ground)

# track bed and rails
fill(x0 - 8, y0 + 1, z0 + 2, x0 + 58, y0 + 1, z0 + 9, "minecraft:gravel")
for x in range(x0 - 8, x0 + 59, 3):
    fill(x, y0 + 2, z0 + 2, x, y0 + 2, z0 + 9, sleeper)

fill(x0 - 8, y0 + 3, z0 + 3, x0 + 58, y0 + 3, z0 + 3, rail)
fill(x0 - 8, y0 + 3, z0 + 8, x0 + 58, y0 + 3, z0 + 8, rail)


def wheels(start_x, end_x):
    for x in range(start_x, end_x + 1, 4):
        fill(x, y0 + 3, z0 + 2, x + 1, y0 + 4, z0 + 2, wheel)
        fill(x, y0 + 3, z0 + 9, x + 1, y0 + 4, z0 + 9, wheel)
        setblock(x, y0 + 4, z0 + 1, "minecraft:stone_button")
        setblock(x, y0 + 4, z0 + 10, "minecraft:stone_button")


def passenger_car(start_x, end_x, color):
    fill(start_x, y0 + 4, z0 + 3, end_x, y0 + 8, z0 + 8, color)
    fill(start_x, y0 + 9, z0 + 3, end_x, y0 + 9, z0 + 8, roof)
    fill(start_x + 1, y0 + 6, z0 + 2, end_x - 1, y0 + 7, z0 + 2, glass)
    fill(start_x + 1, y0 + 6, z0 + 9, end_x - 1, y0 + 7, z0 + 9, glass)
    fill(start_x, y0 + 5, z0 + 5, start_x, y0 + 7, z0 + 6, body_dark)
    fill(end_x, y0 + 5, z0 + 5, end_x, y0 + 7, z0 + 6, body_dark)
    fill(start_x, y0 + 4, z0 + 3, end_x, y0 + 4, z0 + 8, trim)
    wheels(start_x + 1, end_x - 2)


def clear_station():
    fill(x0 - 60, y0 + 2, z0 - 5, x0 + 160, y0 + 14, z0 + 1, air)
    fill(x0 - 60, y0 + 2, z0 + 11, x0 + 160, y0 + 14, z0 + 18, air)


def draw_station(offset):
    sx = x0 + offset

    # far platform
    fill(sx - 6, y0 + 2, z0 + 11, sx + 56, y0 + 3, z0 + 15, platform)
    fill(sx - 6, y0 + 4, z0 + 11, sx + 56, y0 + 4, z0 + 11, trim)
    fill(sx - 6, y0 + 4, z0 + 15, sx + 56, y0 + 4, z0 + 15, trim)

    # near platform. This crosses the camera side and makes the motion obvious.
    fill(sx - 14, y0 + 2, z0 - 5, sx + 66, y0 + 3, z0 - 1, platform)
    fill(sx - 14, y0 + 4, z0 - 1, sx + 66, y0 + 4, z0 - 1, trim)

    # station building
    fill(sx + 8, y0 + 4, z0 + 14, sx + 28, y0 + 10, z0 + 18, "minecraft:brick_block")
    fill(sx + 7, y0 + 11, z0 + 13, sx + 29, y0 + 11, z0 + 18, roof)
    fill(sx + 10, y0 + 6, z0 + 13, sx + 14, y0 + 8, z0 + 13, glass)
    fill(sx + 18, y0 + 6, z0 + 13, sx + 22, y0 + 8, z0 + 13, glass)
    fill(sx + 13, y0 + 11, z0 + 12, sx + 23, y0 + 12, z0 + 12, "minecraft:white_concrete")
    fill(sx + 15, y0 + 12, z0 + 11, sx + 21, y0 + 12, z0 + 11, "minecraft:blue_concrete")

    # posts, lamps, and stripes moving with the station
    for lx in range(sx - 42, sx + 72, 10):
        fill(lx, y0 + 4, z0 - 1, lx, y0 + 13, z0 - 1, "minecraft:iron_bars")
        fill(lx + 1, y0 + 4, z0 - 1, lx + 3, y0 + 4, z0 - 1, "minecraft:white_concrete")

    for lx in range(sx - 34, sx + 70, 16):
        fill(lx, y0 + 4, z0 + 14, lx, y0 + 8, z0 + 14, "minecraft:oak_fence")
        setblock(lx, y0 + 9, z0 + 14, light)


def clear_smoke():
    fill(x0 - 10, y0 + 12, z0 + 3, x0 + 26, y0 + 18, z0 + 8, air)


def draw_smoke(frame):
    drift = frame * 2
    setblock(x0 + drift, y0 + 12, z0 + 5, smoke)
    fill(x0 + drift + 2, y0 + 13, z0 + 5, x0 + drift + 3, y0 + 14, z0 + 6, smoke)
    fill(x0 + drift + 5, y0 + 15, z0 + 4, x0 + drift + 7, y0 + 16, z0 + 6, "minecraft:white_wool")
    fill(x0 + drift + 9, y0 + 16, z0 + 5, x0 + drift + 11, y0 + 17, z0 + 7, smoke)


def clear_track_motion():
    fill(x0 - 60, y0 + 2, z0 + 1, x0 + 160, y0 + 2, z0 + 10, air)


def draw_track_motion(frame):
    shift = (frame * 2) % 6

    for x in range(x0 - 60 + shift, x0 + 161, 6):
        fill(x, y0 + 2, z0 + 2, x + 1, y0 + 2, z0 + 9, sleeper)

    for x in range(x0 - 58 + shift, x0 + 161, 12):
        fill(x, y0 + 2, z0 + 1, x + 2, y0 + 2, z0 + 1, "minecraft:white_concrete")
        fill(x + 5, y0 + 2, z0 + 10, x + 7, y0 + 2, z0 + 10, "minecraft:white_concrete")


def animate_station():
    for frame, offset in enumerate([0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80]):
        clear_station()
        clear_smoke()
        clear_track_motion()
        draw_station(offset)
        draw_smoke(frame % 5)
        draw_track_motion(frame)
        time.sleep(0.05)

    clear_station()
    clear_smoke()
    clear_track_motion()
    draw_station(0)
    draw_smoke(0)
    draw_track_motion(0)


# locomotive base
fill(x0, y0 + 4, z0 + 3, x0 + 14, y0 + 7, z0 + 8, body)
fill(x0 + 3, y0 + 8, z0 + 3, x0 + 10, y0 + 10, z0 + 8, body)
fill(x0 + 4, y0 + 11, z0 + 3, x0 + 9, y0 + 11, z0 + 8, roof)

# boiler and front
fill(x0 - 2, y0 + 5, z0 + 4, x0 + 5, y0 + 7, z0 + 7, body_dark)
fill(x0 - 3, y0 + 5, z0 + 4, x0 - 3, y0 + 7, z0 + 7, metal)
setblock(x0 - 4, y0 + 6, z0 + 5, light)
setblock(x0 - 4, y0 + 6, z0 + 6, light)

# cab windows
fill(x0 + 5, y0 + 9, z0 + 2, x0 + 8, y0 + 10, z0 + 2, glass)
fill(x0 + 5, y0 + 9, z0 + 9, x0 + 8, y0 + 10, z0 + 9, glass)
fill(x0 + 10, y0 + 8, z0 + 4, x0 + 10, y0 + 10, z0 + 7, glass)

# chimney and smoke
fill(x0, y0 + 8, z0 + 5, x0 + 1, y0 + 11, z0 + 6, roof)
draw_smoke(0)

# locomotive decoration and wheels
fill(x0 - 2, y0 + 4, z0 + 3, x0 + 14, y0 + 4, z0 + 8, trim)
fill(x0 + 14, y0 + 5, z0 + 4, x0 + 14, y0 + 6, z0 + 7, body_dark)
wheels(x0 - 1, x0 + 13)

# couplers
fill(x0 + 15, y0 + 5, z0 + 5, x0 + 17, y0 + 5, z0 + 6, metal)
fill(x0 + 34, y0 + 5, z0 + 5, x0 + 36, y0 + 5, z0 + 6, metal)

# passenger cars
passenger_car(x0 + 18, x0 + 33, "minecraft:green_concrete")
passenger_car(x0 + 37, x0 + 52, "minecraft:blue_concrete")

# first station frame
draw_station(0)

# rear lights
setblock(x0 + 53, y0 + 5, z0 + 4, "minecraft:redstone_block")
setblock(x0 + 53, y0 + 5, z0 + 7, "minecraft:redstone_block")

# small signal
fill(x0 + 55, y0 + 4, z0 + 1, x0 + 55, y0 + 10, z0 + 1, metal)
setblock(x0 + 55, y0 + 11, z0 + 1, "minecraft:redstone_block")
setblock(x0 + 55, y0 + 9, z0 + 1, "minecraft:lime_concrete")

# viewing position
#cmd(f"tp @p {x0 + 25} {y0 + 18} {z0 - 18} 0 28")
time.sleep(0.3)
animate_station()
