"""豆腐ハウスで「関数」と「クラス」を学ぶための教材です。"""

import time

from mctools import RCONClient


# Minecraft サーバーに接続します。
mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")


def cmd(command):
    """コマンドと実行結果を画面に表示します。"""
    print(command)
    print(mcr.command(command))


# 家の基本サイズです。どの関数でも同じ値を使います。
WIDTH = 7
DEPTH = 7
HEIGHT = 5
WALL = "oak_planks"
GLASS = "glass"
AIR = "air"


def basehouse(x0, y0, z0):
    """7×7×5 の基本の豆腐ハウスを作ります。"""
    # 床
    cmd(
        f"fill {x0} {y0} {z0} "
        f"{x0 + WIDTH - 1} {y0} {z0 + DEPTH - 1} oak_planks"
    )

    # 正面と背面の壁
    cmd(
        f"fill {x0} {y0 + 1} {z0} "
        f"{x0 + WIDTH - 1} {y0 + HEIGHT} {z0} {WALL}"
    )
    cmd(
        f"fill {x0} {y0 + 1} {z0 + DEPTH - 1} "
        f"{x0 + WIDTH - 1} {y0 + HEIGHT} {z0 + DEPTH - 1} {WALL}"
    )

    # 左右の壁
    cmd(
        f"fill {x0} {y0 + 1} {z0} "
        f"{x0} {y0 + HEIGHT} {z0 + DEPTH - 1} {WALL}"
    )
    cmd(
        f"fill {x0 + WIDTH - 1} {y0 + 1} {z0} "
        f"{x0 + WIDTH - 1} {y0 + HEIGHT} {z0 + DEPTH - 1} {WALL}"
    )

    # 正面中央に、高さ2マスの扉の穴を開けます。
    door_x = x0 + WIDTH // 2
    cmd(f"setblock {door_x} {y0 + 1} {z0} {AIR}")
    cmd(f"setblock {door_x} {y0 + 2} {z0} {AIR}")


def clear_house(x0, y0, z0):
    """家、屋根、5階、周囲の飾りをまとめて消します。"""
    cmd(
        f"fill {x0 - 2} {y0} {z0 - 2} "
        f"{x0 + WIDTH + 1} {y0 + 27} {z0 + DEPTH + 1} {AIR}"
    )


def add_big_window(x0, y0, z0):
    """扉の左右に大きなガラス窓を付けます。"""
    cmd(f"fill {x0 + 1} {y0 + 2} {z0} {x0 + 2} {y0 + 3} {z0} {GLASS}")
    cmd(f"fill {x0 + 4} {y0 + 2} {z0} {x0 + 5} {y0 + 3} {z0} {GLASS}")


def add_flat_roof(x0, y0, z0):
    """家から1マス張り出した平たい屋根を付けます。"""
    cmd(
        f"fill {x0 - 1} {y0 + HEIGHT + 1} {z0 - 1} "
        f"{x0 + WIDTH} {y0 + HEIGHT + 1} {z0 + DEPTH} stone_bricks"
    )


def add_step_roof(x0, y0, z0):
    """3段の簡単な段々屋根を付けます。"""
    # 段が上がるたびに、X方向の幅を左右から1マスずつ狭くします。
    for step in range(3):
        cmd(
            f"fill {x0 - 1 + step} {y0 + HEIGHT + 1 + step} {z0 - 1} "
            f"{x0 + WIDTH - step} {y0 + HEIGHT + 1 + step} "
            f"{z0 + DEPTH} stone_bricks"
        )


def add_roof(x0, y0, z0, roof_type="flat"):
    """引数 roof_type で屋根のパターンを切り替えます。"""
    if roof_type == "step":
        add_step_roof(x0, y0, z0)
    else:
        # "flat" と、不明な値は平たい屋根にします。
        add_flat_roof(x0, y0, z0)


def clear_roof(x0, y0, z0):
    """平屋根と段々屋根が入る範囲だけを消します。"""
    cmd(
        f"fill {x0 - 1} {y0 + HEIGHT + 1} {z0 - 1} "
        f"{x0 + WIDTH} {y0 + HEIGHT + 3} {z0 + DEPTH} {AIR}"
    )


def _add_upper_floor(x0, y0, z0):
    """2階以上を作るための、教材内部用の小さな関数です。"""
    # 上の階の床と4枚の壁を作ります。
    cmd(
        f"fill {x0} {y0} {z0} "
        f"{x0 + WIDTH - 1} {y0} {z0 + DEPTH - 1} oak_planks"
    )
    cmd(
        f"fill {x0} {y0 + 1} {z0} "
        f"{x0 + WIDTH - 1} {y0 + HEIGHT} {z0} {WALL}"
    )
    cmd(
        f"fill {x0} {y0 + 1} {z0 + DEPTH - 1} "
        f"{x0 + WIDTH - 1} {y0 + HEIGHT} {z0 + DEPTH - 1} {WALL}"
    )
    cmd(
        f"fill {x0} {y0 + 1} {z0} "
        f"{x0} {y0 + HEIGHT} {z0 + DEPTH - 1} {WALL}"
    )
    cmd(
        f"fill {x0 + WIDTH - 1} {y0 + 1} {z0} "
        f"{x0 + WIDTH - 1} {y0 + HEIGHT} {z0 + DEPTH - 1} {WALL}"
    )

    # 上の階には、正面中央に小さな窓を付けます。
    cmd(f"fill {x0 + 2} {y0 + 2} {z0} {x0 + 4} {y0 + 3} {z0} {GLASS}")


def add_second_floor(x0, y0, z0):
    """基本の家の上に2階部分を追加します。"""
    _add_upper_floor(x0, y0 + HEIGHT, z0)


def add_floors(x0, y0, z0, floors=1):
    """floors の数だけ階を積み上げます（最大5階）。"""
    # 教材が重くなりすぎないよう、1～5の範囲にします。
    floors = max(1, min(floors, 5))
    basehouse(x0, y0, z0)

    # floor_number が 2、3 と増えるたび、5マス上に積みます。
    for floor_number in range(2, floors + 1):
        floor_y = y0 + HEIGHT * (floor_number - 1)
        _add_upper_floor(x0, floor_y, z0)


def add_decoration_blocks(x0, y0, z0):
    """光るブロックを家の前に置きます。"""
    cmd(f"setblock {x0 + 1} {y0 + 1} {z0 - 1} sea_lantern")
    cmd(f"setblock {x0 + WIDTH - 2} {y0 + 1} {z0 - 1} sea_lantern")


def add_green_decoration(x0, y0, z0):
    """葉っぱを正面と側面に少しだけ飾ります。"""
    cmd(f"fill {x0 - 1} {y0 + 1} {z0} {x0 - 1} {y0 + 2} {z0 + 1} oak_leaves")
    cmd(
        f"fill {x0 + WIDTH} {y0 + 1} {z0 + DEPTH - 2} "
        f"{x0 + WIDTH} {y0 + 2} {z0 + DEPTH - 1} oak_leaves"
    )


def add_decoration(x0, y0, z0, decoration_type="none"):
    """引数 decoration_type で飾りのパターンを切り替えます。"""
    if decoration_type == "blocks":
        add_decoration_blocks(x0, y0, z0)
    elif decoration_type == "green":
        add_green_decoration(x0, y0, z0)
    # "none" と不明な値では、何も置きません。


def clear_decoration(x0, y0, z0):
    """この教材で置いた飾りだけを消します。"""
    # 家の前に置いた sea_lantern を消します。
    cmd(f"setblock {x0 + 1} {y0 + 1} {z0 - 1} {AIR}")
    cmd(f"setblock {x0 + WIDTH - 2} {y0 + 1} {z0 - 1} {AIR}")

    # 家の左右に置いた oak_leaves を消します。
    cmd(f"fill {x0 - 1} {y0 + 1} {z0} {x0 - 1} {y0 + 2} {z0 + 1} {AIR}")
    cmd(
        f"fill {x0 + WIDTH} {y0 + 1} {z0 + DEPTH - 2} "
        f"{x0 + WIDTH} {y0 + 2} {z0 + DEPTH - 1} {AIR}"
    )


def change_decoration_every_second(x0, y0, z0, repeat=3):
    """同じ家の飾りと屋根を1秒ごとに切り替えます。"""
    patterns = [
        # 飾り,    屋根
        ("blocks", "flat"),
        ("green", "step"),
        ("none", "flat"),
    ]

    # repeat=3 なら、3種類の変化を3周します。
    for _ in range(repeat):
        for decoration_type, roof_type in patterns:
            # 前の飾りと屋根を消してから、次のパターンを置きます。
            clear_decoration(x0, y0, z0)
            clear_roof(x0, y0, z0)
            add_decoration(x0, y0, z0, decoration_type)
            add_roof(x0, y0, z0, roof_type)
            print(f"現在の飾り: {decoration_type} / 屋根: {roof_type}")
            time.sleep(1)


def grow_to_five_floors(x0, y0, z0, interval=1):
    """同じ座標の家を、1秒間隔で5階まで伸ばします。"""
    # 最初に1階を作ります。
    basehouse(x0, y0, z0)
    add_big_window(x0, y0, z0)

    # 1秒待つたびに、同じ家の上へ次の階を追加します。
    for floor_number in range(2, 6):
        time.sleep(interval)
        floor_y = y0 + HEIGHT * (floor_number - 1)
        _add_upper_floor(x0, floor_y, z0)
        print(f"{floor_number}階まで伸びました")

    # 最後に5階の上へ屋根を載せます。
    top_floor_y = y0 + HEIGHT * 4
    add_flat_roof(x0, top_floor_y, z0)


class House:
    """座標を覚えていて、同じ家に部品を追加できるオブジェクトです。"""

    def __init__(self, x0, y0, z0):
        # self に保存すると、別のメソッドから同じ座標を使えます。
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.width = WIDTH
        self.depth = DEPTH
        self.height = HEIGHT

    def build(self):
        """基本の家を作ります。"""
        basehouse(self.x0, self.y0, self.z0)

    def clear(self):
        """この家を消します。"""
        clear_house(self.x0, self.y0, self.z0)

    def add_window(self):
        """この家に大きな窓を付けます。"""
        add_big_window(self.x0, self.y0, self.z0)

    def add_roof(self, roof_type="flat"):
        """この家に指定した屋根を付けます。"""
        add_roof(self.x0, self.y0, self.z0, roof_type)

    def add_floors(self, floors=1):
        """この座標に、指定した階数の家を作ります。"""
        add_floors(self.x0, self.y0, self.z0, floors)

    def add_decoration(self, decoration_type="none"):
        """この家に指定した飾りを付けます。"""
        add_decoration(self.x0, self.y0, self.z0, decoration_type)

    def change_decoration_every_second(self, repeat=3):
        """同じ家の飾りと屋根を1秒ごとに切り替えます。"""
        change_decoration_every_second(self.x0, self.y0, self.z0, repeat)

    def grow_to_five_floors(self, interval=1):
        """同じ家を、指定した秒数の間隔で5階まで伸ばします。"""
        grow_to_five_floors(self.x0, self.y0, self.z0, interval)

    def build_custom(
        self,
        floors=1,
        roof_type="flat",
        decoration_type="none",
        window=True,
    ):
        """引数を組み合わせて、好みの家をまとめて作ります。"""
        floors = max(1, min(floors, 5))

        # まず家本体を指定した階数まで作ります。
        add_floors(self.x0, self.y0, self.z0, floors)

        if window:
            add_big_window(self.x0, self.y0, self.z0)

        # 最上階の高さを屋根関数の基準座標として渡します。
        roof_y = self.y0 + HEIGHT * (floors - 1)
        add_roof(self.x0, roof_y, self.z0, roof_type)
        add_decoration(self.x0, self.y0, self.z0, decoration_type)


def build_house_town(x0=0, y0=0, z0=0, interval=1):
    """約50×50の範囲に、違う家を1件ずつ建てます。"""
    # x と z は基準座標からの移動量です。
    # 4列×3行に並べても、家同士が重ならない間隔にしています。
    house_patterns = [
        # x,  z, 階数, 屋根,   飾り,    大きな窓
        (1, 1, 1, "flat", "none", True),
        (13, 1, 1, "step", "green", True),
        (25, 1, 2, "flat", "blocks", True),
        (37, 1, 2, "step", "none", False),
        (1, 15, 1, "step", "blocks", False),
        (13, 15, 2, "flat", "green", True),
        (25, 15, 3, "step", "none", True),
        (37, 15, 1, "flat", "green", False),
        (1, 29, 2, "step", "blocks", True),
        (13, 29, 3, "flat", "none", False),
        (25, 29, 1, "flat", "blocks", True),
        (37, 29, 2, "step", "green", True),
    ]

    total = len(house_patterns)

    # リストから設定を1件ずつ取り出します。
    for number, pattern in enumerate(house_patterns, start=1):
        dx, dz, floors, roof_type, decoration_type, window = pattern

        # House オブジェクトを作り、覚えさせる座標を変えます。
        house = House(x0 + dx, y0, z0 + dz)
        house.build_custom(
            floors=floors,
            roof_type=roof_type,
            decoration_type=decoration_type,
            window=window,
        )
        print(f"{number}件目の家が建ちました")

        # 最後の家を建てた後は待ちません。
        if number < total:
            time.sleep(interval)


# -------------------------------------------------------------------
# 実行例
# 一度にたくさん作らないよう、最初の例だけを有効にしています。
# 試したい例の先頭にある「#」を外してください。
# -------------------------------------------------------------------


#以下のコードは何が違うか考えよう
# basehouse(0,0,0)
# 　と
# house_sample = House(0, 0, 0)
# house_sample.build()


#装飾がかわる豆腐ハウス
# house_sample = House(0, 0, 0)
# house_sample.build()
# house_sample.add_window()
# house_sample.change_decoration_every_second(repeat=3)


#伸びる豆腐ハウス
# grow_to_five_floors(0, 0, 0, interval=1)

# 約50×50の住宅街を、1秒間隔で1件ずつ作る例（この例だけ有効）
build_house_town(0, 0, 0, interval=1)

