import time
from mctools import RCONClient

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")


def cmd(command):
    print(command)
    print(mcr.command(command))
    time.sleep(0.003)


def fill(x1, y1, z1, x2, y2, z2, block):
    cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}")


def setblock(x, y, z, block):
    cmd(f"setblock {x} {y} {z} {block}")


def clone(x1, y1, z1, x2, y2, z2, x, y, z):
    cmd(f"clone {x1} {y1} {z1} {x2} {y2} {z2} {x} {y} {z} masked normal")


x0 = 0
y0 = 0
z0 = 0

air = "minecraft:air"
ground = "minecraft:grass_block"
gravel = "minecraft:gravel"
rail = "minecraft:iron_block"
sleeper = "minecraft:dark_oak_planks"
body = "minecraft:green_concrete"
body_dark = "minecraft:green_terracotta"
door = "minecraft:orange_concrete"
door_dark = "minecraft:brown_concrete"
roof = "minecraft:red_nether_bricks"
window = "minecraft:light_blue_stained_glass"
black = "minecraft:black_concrete"
white = "minecraft:white_concrete"
yellow = "minecraft:yellow_concrete"
metal = "minecraft:iron_block"
bar = "minecraft:iron_bars"
lamp = "minecraft:sea_lantern"
platform = "minecraft:smooth_stone"

track_start = x0 - 35
track_end = x0 + 210
car_length = 64
template_x = x0
template_z = z0 + 50


def draw_track(start_x, end_x):
    fill(start_x, y0 + 1, z0 + 2, end_x, y0 + 1, z0 + 9, gravel)

    first_sleeper = start_x - (start_x % 3)
    for x in range(first_sleeper, end_x + 1, 3):
        fill(x, y0 + 2, z0 + 2, x, y0 + 2, z0 + 9, sleeper)

    fill(start_x, y0 + 3, z0 + 3, end_x, y0 + 3, z0 + 3, rail)
    fill(start_x, y0 + 3, z0 + 8, end_x, y0 + 3, z0 + 8, rail)


def draw_scenery():
    fill(x0 - 40, y0, z0 - 10, x0 + 215, y0, z0 + 20, ground)
    draw_track(track_start, track_end)

    fill(track_start, y0 + 2, z0 - 3, track_end, y0 + 3, z0 + 0, platform)
    fill(track_start, y0 + 4, z0 + 0, track_end, y0 + 4, z0 + 0, yellow)

    for lx in range(track_start + 8, track_end, 18):
        fill(lx, y0 + 4, z0 - 2, lx, y0 + 9, z0 - 2, "minecraft:oak_fence")
        setblock(lx, y0 + 10, z0 - 2, lamp)

    for px in range(track_start + 6, track_end + 1, 28):
        fill(px, y0 + 2, z0 + 12, px, y0 + 24, z0 + 12, metal)
        fill(px, y0 + 22, z0 + 7, px, y0 + 22, z0 + 12, metal)

    fill(track_start, y0 + 22, z0 + 7, track_end, y0 + 22, z0 + 7, bar)


def wheels(base_x, base_z):
    for x in range(base_x + 5, base_x + 52, 7):
        fill(x, y0 + 3, base_z + 2, x + 2, y0 + 4, base_z + 2, black)
        fill(x, y0 + 3, base_z + 9, x + 2, y0 + 4, base_z + 9, black)
        fill(x, y0 + 4, base_z + 1, x + 2, y0 + 4, base_z + 1, metal)
        fill(x, y0 + 4, base_z + 10, x + 2, y0 + 4, base_z + 10, metal)


def side_windows(base_x, base_z, side_z):
    for sx in [base_x + 6, base_x + 11, base_x + 21, base_x + 26, base_x + 31, base_x + 41, base_x + 46, base_x + 51]:
        fill(sx, y0 + 8, base_z + side_z, sx + 3, y0 + 10, base_z + side_z, window)
        fill(sx, y0 + 11, base_z + side_z, sx + 3, y0 + 11, base_z + side_z, black)


def make_front(x, base_z):
    fill(x, y0 + 5, base_z + 4, x, y0 + 12, base_z + 7, body_dark)
    fill(x, y0 + 8, base_z + 4, x, y0 + 10, base_z + 7, window)
    fill(x, y0 + 11, base_z + 4, x, y0 + 12, base_z + 7, black)
    setblock(x, y0 + 13, base_z + 5, lamp)
    setblock(x, y0 + 13, base_z + 6, lamp)
    fill(x, y0 + 6, base_z + 4, x, y0 + 6, base_z + 7, black)
    fill(x, y0 + 5, base_z + 5, x, y0 + 5, base_z + 6, yellow)
    setblock(x, y0 + 5, base_z + 4, yellow)
    setblock(x, y0 + 5, base_z + 7, yellow)


def make_pantograph(base_x, base_z):
    fill(base_x + 24, y0 + 14, base_z + 4, base_x + 36, y0 + 14, base_z + 7, black)
    fill(base_x + 25, y0 + 15, base_z + 5, base_x + 25, y0 + 19, base_z + 6, bar)
    fill(base_x + 35, y0 + 15, base_z + 5, base_x + 35, y0 + 19, base_z + 6, bar)

    for i in range(0, 6):
        setblock(base_x + 25 + i, y0 + 15 + i, base_z + 5, bar)
        setblock(base_x + 25 + i, y0 + 15 + i, base_z + 6, bar)
        setblock(base_x + 35 - i, y0 + 15 + i, base_z + 5, bar)
        setblock(base_x + 35 - i, y0 + 15 + i, base_z + 6, bar)

    fill(base_x + 27, y0 + 21, base_z + 5, base_x + 33, y0 + 21, base_z + 6, metal)


def draw_train(base_x, base_z):
    fill(base_x + 2, y0 + 5, base_z + 3, base_x + 58, y0 + 11, base_z + 8, body)
    fill(base_x + 3, y0 + 4, base_z + 3, base_x + 57, y0 + 4, base_z + 8, body_dark)
    fill(base_x + 3, y0 + 12, base_z + 3, base_x + 57, y0 + 14, base_z + 8, roof)
    fill(base_x + 6, y0 + 15, base_z + 4, base_x + 54, y0 + 15, base_z + 7, roof)
    fill(base_x + 12, y0 + 16, base_z + 5, base_x + 48, y0 + 16, base_z + 6, roof)

    for door_x in [base_x + 16, base_x + 36]:
        fill(door_x, y0 + 5, base_z + 2, door_x + 3, y0 + 11, base_z + 2, door)
        fill(door_x, y0 + 5, base_z + 9, door_x + 3, y0 + 11, base_z + 9, door)
        fill(door_x + 1, y0 + 6, base_z + 2, door_x + 2, y0 + 9, base_z + 2, door_dark)
        fill(door_x + 1, y0 + 6, base_z + 9, door_x + 2, y0 + 9, base_z + 9, door_dark)

    side_windows(base_x, base_z, 2)
    side_windows(base_x, base_z, 9)
    fill(base_x + 3, y0 + 7, base_z + 2, base_x + 57, y0 + 7, base_z + 2, black)
    fill(base_x + 3, y0 + 7, base_z + 9, base_x + 57, y0 + 7, base_z + 9, black)
    fill(base_x + 3, y0 + 12, base_z + 2, base_x + 57, y0 + 12, base_z + 2, black)
    fill(base_x + 3, y0 + 12, base_z + 9, base_x + 57, y0 + 12, base_z + 9, black)

    make_front(base_x + 1, base_z)
    make_front(base_x + 59, base_z)

    fill(base_x + 1, y0 + 12, base_z + 5, base_x + 1, y0 + 12, base_z + 6, white)
    fill(base_x + 59, y0 + 12, base_z + 5, base_x + 59, y0 + 12, base_z + 6, white)
    setblock(base_x + 1, y0 + 13, base_z + 4, black)
    setblock(base_x + 59, y0 + 13, base_z + 7, black)

    fill(base_x + 2, y0 + 4, base_z + 4, base_x + 58, y0 + 4, base_z + 7, black)
    wheels(base_x, base_z)
    fill(base_x - 1, y0 + 5, base_z + 5, base_x + 1, y0 + 5, base_z + 6, metal)
    fill(base_x + 59, y0 + 5, base_z + 5, base_x + 61, y0 + 5, base_z + 6, metal)

    setblock(base_x + 1, y0 + 5, base_z + 3, yellow)
    setblock(base_x + 1, y0 + 6, base_z + 3, yellow)
    setblock(base_x + 2, y0 + 5, base_z + 3, yellow)
    setblock(base_x + 59, y0 + 5, base_z + 8, yellow)
    setblock(base_x + 59, y0 + 6, base_z + 8, yellow)
    setblock(base_x + 58, y0 + 5, base_z + 8, yellow)

    make_pantograph(base_x, base_z)


def clear_moving_train(base_x):
    # Leave the rails at y=3, z=3 and z=8 untouched.
    fill(base_x - 3, y0 + 4, z0 + 1, base_x + car_length, y0 + 21, z0 + 10, air)
    fill(base_x - 3, y0 + 3, z0 + 1, base_x + car_length, y0 + 3, z0 + 2, air)
    fill(base_x - 3, y0 + 3, z0 + 9, base_x + car_length, y0 + 3, z0 + 10, air)


def clone_train(base_x):
    clone(template_x - 3, y0 + 3, template_z + 1, template_x + car_length, y0 + 21, template_z + 10, base_x - 3, y0 + 3, z0 + 1)


def animate_train():
    positions = range(x0 - 22, x0 + 136, 4)
    previous = None

    for pos in positions:
        if previous is not None:
            clear_moving_train(previous)
        clone_train(pos)
        previous = pos
        time.sleep(0.08)

    time.sleep(0.4)


# Keep every fill below Minecraft's 32,768-block command limit.
for clear_x in range(x0 - 40, x0 + 216, 32):
    fill(clear_x, y0, z0 - 10, min(clear_x + 31, x0 + 215), y0 + 28, z0 + 20, air)

fill(template_x - 4, y0 + 3, template_z, template_x + car_length, y0 + 21, template_z + 11, air)
draw_scenery()
draw_train(template_x, template_z)
animate_train()

# Viewing position
# cmd(f"tp @p {x0 + 55} {y0 + 22} {z0 - 28} 0 28")
