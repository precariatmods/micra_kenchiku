import time

from mctools import RCONClient


# ----- RCON接続設定 -----
RCON_HOST = "192.168.1.10"
RCON_PORT = 25575
RCON_PASSWORD = "サーバーで設定したRCONパスワード"

# ----- 建築設定（見た目を変えたいときは主にここを調整）-----
START_X = 0
START_Y = 0
START_Z = 0
RAIL_LENGTH = 80
RISE_EVERY = 4
POWERED_INTERVAL = 8
BUILD_DELAY = 0.05
STARTER_LENGTH = 12
COUNTDOWN_SECONDS = 3
PLAYER_SELECTOR = "@p"

SUPPORT_BLOCK = "minecraft:smooth_stone"
POWER_BLOCK = "minecraft:redstone_block"
BUMPER_BLOCK = "minecraft:iron_block"
CLEAR_SPACE = True


mcr = RCONClient(RCON_HOST, port=RCON_PORT)
mcr.login(RCON_PASSWORD)


def cmd(command):
    """Minecraftへコマンドを送り、実行結果を表示する。"""
    print(command)
    print(mcr.command(command))


def clear_build_space(x0, y0, z0, length, rise_every):
    """レールの周囲を空気にして、伸びる様子を見やすくする。"""
    highest_y = y0 + (length - 1) // rise_every
    cmd(
        f"fill {x0 - 1} {y0} {z0 - 2} "
        f"{x0 + length} {highest_y + 3} {z0 + 2} minecraft:air"
    )


def build_rising_rail(
    x0,
    y0,
    z0,
    length=80,
    rise_every=4,
    powered_interval=8,
    delay=0.05,
):
    """プレイヤーを乗せ、前方へ伸びるレールを建築する。"""
    if length < 1:
        raise ValueError("length は1以上にしてください")
    if rise_every < 2:
        raise ValueError("rise_every は2以上にしてください")
    if powered_interval < 1:
        raise ValueError("powered_interval は1以上にしてください")
    if delay < 0:
        raise ValueError("delay は0以上にしてください")

    # 背面のブロックに押し出されるため、先頭のトロッコが発進しやすくなる。
    cmd(f"setblock {x0 - 1} {y0} {z0} {BUMPER_BLOCK}")

    starter_length = min(STARTER_LENGTH, length)

    # 発進前に短い助走区間を作り、トロッコが線路へ追いつかないようにする。
    for step in range(starter_length):
        place_rail_segment(
            x0,
            y0,
            z0,
            step,
            length,
            rise_every,
            powered_interval,
            lock_start=True,
        )

    place_minecart(x0, y0, z0)
    cmd(
        f"ride {PLAYER_SELECTOR} mount "
        "@e[type=minecraft:minecart,sort=nearest,limit=1]"
    )

    for count in range(COUNTDOWN_SECONDS, 0, -1):
        cmd(f"title {PLAYER_SELECTOR} actionbar \"レール生成開始まで {count}\"")
        time.sleep(1)

    # 先頭のパワードレールを給電すると、背面ブロックの反対側へ発進する。
    cmd(f"setblock {x0} {y0 - 1} {z0} {POWER_BLOCK}")
    cmd(
        f"setblock {x0} {y0} {z0} "
        "minecraft:powered_rail[shape=east_west,powered=true]"
    )
    cmd(f"title {PLAYER_SELECTOR} actionbar \"出発！\"")

    # トロッコの前を追いかけるように、残りのレールをテンポよく伸ばす。
    for step in range(starter_length, length):
        place_rail_segment(
            x0,
            y0,
            z0,
            step,
            length,
            rise_every,
            powered_interval,
        )
        time.sleep(delay)


def place_rail_segment(
    x0,
    y0,
    z0,
    step,
    length,
    rise_every,
    powered_interval,
    lock_start=False,
):
    """支えとレールを1区画だけ設置する。"""
    x = x0 + step
    y = y0 + step // rise_every

    # 次のレールが1段高い場合、この位置を上り坂にする。
    next_y = y0 + (step + 1) // rise_every
    is_rising = step < length - 1 and next_y > y
    rail_shape = "ascending_east" if is_rising else "east_west"

    is_powered = step % powered_interval == 0
    if is_powered:
        # レッドストーンブロックは支えと電源を兼ね、位置も目立つ。
        # 先頭だけは乗車が終わるまで給電せず、トロッコを停止させておく。
        support_block = (
            SUPPORT_BLOCK if lock_start and step == 0 else POWER_BLOCK
        )
        rail_block = "minecraft:powered_rail"
    else:
        support_block = SUPPORT_BLOCK
        rail_block = "minecraft:rail"

    # 必ず支えを先に置いてから、その上にレールを置く。
    cmd(f"setblock {x} {y - 1} {z0} {support_block}")
    cmd(f"setblock {x} {y} {z0} {rail_block}[shape={rail_shape}]")


def place_minecart(x, y, z):
    """開始レールの中央にトロッコを置く。"""
    cmd(f"summon minecraft:minecart {x + 0.5} {y + 0.1} {z + 0.5}")


def remove_all_minecarts():
    """ワールド内にある通常のトロッコをすべて削除する。"""
    cmd("kill @e[type=minecraft:minecart]")


def main():
    remove_all_minecarts()

    if CLEAR_SPACE:
        clear_build_space(
            START_X,
            START_Y,
            START_Z,
            RAIL_LENGTH,
            RISE_EVERY,
        )

    build_rising_rail(
        START_X,
        START_Y,
        START_Z,
        length=RAIL_LENGTH,
        rise_every=RISE_EVERY,
        powered_interval=POWERED_INTERVAL,
        delay=BUILD_DELAY,
    )


if __name__ == "__main__":
    main()


# 調整ポイント:
# RAIL_LENGTH       : レール全体の長さ
# RISE_EVERY        : 何ブロック進むごとに1段上がるか
# POWERED_INTERVAL  : パワードレールを置く間隔
# BUILD_DELAY       : 1区画ごとの待ち時間（小さいほど速い）
# STARTER_LENGTH    : 発進前に先に作っておくレールの長さ
# PLAYER_SELECTOR   : 乗車させるプレイヤー（名前を直接指定してもよい）
