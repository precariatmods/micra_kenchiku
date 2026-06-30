import time
from mctools import RCONClient

# ============================================================
# RCON 接続
# ============================================================

mcr = RCONClient("192.168.1.10", port=25575)
mcr.login("サーバーで設定したRCONパスワード")


def cmd(command):
    print(command)
    print(mcr.command(command))


# ------------------------------------------------------------
# 補助関数
# ------------------------------------------------------------

def fill(x1, y1, z1, x2, y2, z2, block):
    cmd(f"fill {x1} {y1} {z1} {x2} {y2} {z2} {block}")


def setblock(x, y, z, block):
    cmd(f"setblock {x} {y} {z} {block}")


# ============================================================
# 鯛よし百番 V字平面版
#
# サイズ目安：
#   幅 約50
#   奥行 約45
#   高さ 約35
#
# 前面：
#   z = -24 側
#
# 平面イメージ：
#
#          奥
#          ↑
#
#      ／￣￣￣￣＼
#    ／              ＼
#  ／                  ＼
#  ───── 正面 ─────
#
# 正面中央だけ短くまっすぐ。
# 左右の外壁・欄干・提灯列が奥へ斜めに伸びる。
# ============================================================


# ------------------------------------------------------------
# ブロック設定
# ------------------------------------------------------------

AIR        = "minecraft:air"

BASE       = "minecraft:smooth_stone"
STONE      = "minecraft:stone_bricks"

WOOD       = "minecraft:spruce_planks"
DARK_WOOD  = "minecraft:dark_oak_planks"
LOG        = "minecraft:dark_oak_log"

RED        = "minecraft:red_concrete"
DARK_RED   = "minecraft:red_nether_bricks"

BLACK      = "minecraft:black_concrete"
WHITE      = "minecraft:white_concrete"
GOLD       = "minecraft:gold_block"

PAPER      = "minecraft:birch_planks"
GLASS      = "minecraft:glass"

ROOF       = "minecraft:deepslate_tiles"
ROOF_EDGE  = "minecraft:polished_blackstone_bricks"

LAMP       = "minecraft:glowstone"
LANTERN    = "minecraft:sea_lantern"
ORANGE     = "minecraft:orange_concrete"

cmd("time set day")

# ------------------------------------------------------------
# V字平面の幅を決める関数
# z=-24 では正面が狭く、奥へ行くほど広くなる
# ------------------------------------------------------------

def half_width(z):
    # z = -24 のとき 7
    # z = 18  のとき 25 くらい
    return 7 + int((z + 24) * 0.43)


# ------------------------------------------------------------
# 1. 敷地・石畳
# ------------------------------------------------------------

fill(-28, 0, -28, 28, 0, 24, BASE)

time.sleep(0.5)


# ------------------------------------------------------------
# 2. V字型の床
# ------------------------------------------------------------

for z in range(-24, 19):
    hw = half_width(z)
    fill(-hw, 1, z, hw, 1, z, DARK_WOOD)

time.sleep(0.5)


# ------------------------------------------------------------
# 3. 一階の外壁
# ------------------------------------------------------------

# 正面中央の短い壁
fill(-7, 2, -24, 7, 10, -24, WOOD)

# 左右の斜め壁
for z in range(-23, 19):
    hw = half_width(z)

    # 左壁
    fill(-hw, 2, z, -hw, 10, z, WOOD)

    # 右壁
    fill(hw, 2, z, hw, 10, z, WOOD)

# 奥の壁
hw_back = half_width(18)
fill(-hw_back, 2, 18, hw_back, 10, 18, WOOD)

time.sleep(0.5)


# ------------------------------------------------------------
# 4. 一階内部を軽く抜く
# ------------------------------------------------------------

for z in range(-21, 16):
    hw = half_width(z) - 2
    fill(-hw, 3, z, hw, 9, z, AIR)

time.sleep(0.5)


# ------------------------------------------------------------
# 5. 一階の柱
# ------------------------------------------------------------

# 正面柱
for x in [-7, -3, 3, 7]:
    fill(x, 1, -24, x, 11, -24, LOG)

# 斜め壁の柱
for z in range(-20, 17, 6):
    hw = half_width(z)
    fill(-hw, 1, z, -hw, 11, z, LOG)
    fill(hw, 1, z, hw, 11, z, LOG)

# 奥柱
for x in [-22, -12, 0, 12, 22]:
    fill(x, 1, 18, x, 11, 18, LOG)

time.sleep(0.5)


# ------------------------------------------------------------
# 6. 正面入口
# ------------------------------------------------------------

# 入口を抜く
fill(-4, 2, -24, 4, 7, -24, AIR)

# ガラス戸
fill(-3, 2, -25, -1, 6, -25, GLASS)
fill(1, 2, -25, 3, 6, -25, GLASS)

# 玄関マット
fill(-4, 1, -28, 4, 1, -25, RED)

# 入口左右の明かり
setblock(-6, 5, -25, LAMP)
setblock(6, 5, -25, LAMP)

time.sleep(0.5)


# ------------------------------------------------------------
# 7. 正面の黒金看板
# ------------------------------------------------------------

# 黒い看板
fill(-9, 9, -25, 9, 12, -25, BLACK)

# 金文字風
fill(-7, 10, -26, -4, 11, -26, GOLD)
fill(-1, 10, -26, 1, 11, -26, GOLD)
fill(4, 10, -26, 7, 11, -26, GOLD)

# 看板の縁
fill(-10, 8, -25, 10, 8, -25, ROOF_EDGE)
fill(-10, 13, -25, 10, 13, -25, ROOF_EDGE)
fill(-10, 8, -25, -10, 13, -25, ROOF_EDGE)
fill(10, 8, -25, 10, 13, -25, ROOF_EDGE)

time.sleep(0.5)


# ------------------------------------------------------------
# 8. 唐破風風の正面装飾
# ------------------------------------------------------------

# 黒い曲線風を階段状に作る
fill(-12, 12, -25, 12, 12, -25, BLACK)
fill(-10, 13, -25, 10, 13, -25, BLACK)
fill(-7, 14, -25, 7, 14, -25, BLACK)
fill(-4, 15, -25, 4, 15, -25, BLACK)

# 白い縁取り
fill(-13, 12, -26, -13, 12, -26, WHITE)
fill(13, 12, -26, 13, 12, -26, WHITE)

fill(-11, 13, -26, -11, 13, -26, WHITE)
fill(11, 13, -26, 11, 13, -26, WHITE)

fill(-8, 14, -26, -8, 14, -26, WHITE)
fill(8, 14, -26, 8, 14, -26, WHITE)

fill(-5, 15, -26, -5, 15, -26, WHITE)
fill(5, 15, -26, 5, 15, -26, WHITE)

# 中央金装飾
setblock(0, 14, -26, GOLD)
setblock(-1, 13, -26, GOLD)
setblock(1, 13, -26, GOLD)

time.sleep(0.5)


# ------------------------------------------------------------
# 9. 二階床
# ------------------------------------------------------------

for z in range(-24, 19):
    hw = half_width(z)
    fill(-hw, 13, z, hw, 13, z, DARK_WOOD)

time.sleep(0.5)


# ------------------------------------------------------------
# 10. 二階の外壁
# ------------------------------------------------------------

# 正面二階壁
fill(-7, 14, -24, 7, 21, -24, WOOD)

# 斜め二階壁
for z in range(-23, 19):
    hw = half_width(z)
    fill(-hw, 14, z, -hw, 21, z, WOOD)
    fill(hw, 14, z, hw, 21, z, WOOD)

# 奥二階壁
fill(-hw_back, 14, 18, hw_back, 21, 18, WOOD)

# 中を抜く
for z in range(-21, 16):
    hw = half_width(z) - 2
    fill(-hw, 15, z, hw, 20, z, AIR)

time.sleep(0.5)


# ------------------------------------------------------------
# 11. 二階柱
# ------------------------------------------------------------

# 正面
for x in [-7, -3, 3, 7]:
    fill(x, 13, -24, x, 22, -24, LOG)

# 斜め
for z in range(-20, 17, 6):
    hw = half_width(z)
    fill(-hw, 13, z, -hw, 22, z, LOG)
    fill(hw, 13, z, hw, 22, z, LOG)

# 奥
for x in [-22, -12, 0, 12, 22]:
    fill(x, 13, 18, x, 22, 18, LOG)

time.sleep(0.5)


# ------------------------------------------------------------
# 12. V字に沿った赤い二階ベランダ
# ------------------------------------------------------------

# 正面ベランダ床
fill(-12, 14, -28, 12, 14, -25, DARK_WOOD)

# 正面手すり
fill(-12, 15, -28, 12, 15, -28, RED)
fill(-12, 17, -28, 12, 17, -28, RED)

for x in range(-12, 13, 4):
    fill(x, 15, -28, x, 18, -28, RED)

# 左右斜めベランダ
for z in range(-24, 17):
    hw = half_width(z)

    # 左側ベランダ床
    fill(-hw - 3, 14, z, -hw - 1, 14, z, DARK_WOOD)

    # 右側ベランダ床
    fill(hw + 1, 14, z, hw + 3, 14, z, DARK_WOOD)

    # 左手すり
    fill(-hw - 3, 15, z, -hw - 3, 17, z, RED)

    # 右手すり
    fill(hw + 3, 15, z, hw + 3, 17, z, RED)

# 手すりの横線を補強
for z in range(-24, 17, 2):
    hw = half_width(z)
    setblock(-hw - 3, 16, z, RED)
    setblock(hw + 3, 16, z, RED)

time.sleep(0.5)


# ------------------------------------------------------------
# 13. V字に沿った提灯列
# ------------------------------------------------------------

# 正面提灯列
fill(-13, 19, -29, 13, 20, -29, RED)

for x in range(-12, 13, 4):
    setblock(x, 18, -30, ORANGE)
    setblock(x, 19, -30, LANTERN)
    setblock(x, 20, -30, ORANGE)

# 左右斜めの赤い帯と提灯
for z in range(-23, 17):
    hw = half_width(z)

    # 赤い帯
    setblock(-hw - 4, 20, z, RED)
    setblock(hw + 4, 20, z, RED)

# 提灯は間隔を空けて配置
for z in range(-22, 16, 4):
    hw = half_width(z)

    # 左側
    setblock(-hw - 5, 18, z, ORANGE)
    setblock(-hw - 5, 19, z, LANTERN)
    setblock(-hw - 5, 20, z, ORANGE)

    # 右側
    setblock(hw + 5, 18, z, ORANGE)
    setblock(hw + 5, 19, z, LANTERN)
    setblock(hw + 5, 20, z, ORANGE)

time.sleep(0.5)


# ------------------------------------------------------------
# 14. 障子・窓
# ------------------------------------------------------------

# 正面二階の障子
for x in [-4, 4]:
    fill(x - 2, 16, -25, x + 2, 20, -25, PAPER)
    fill(x, 16, -26, x, 20, -26, LOG)
    fill(x - 2, 18, -26, x + 2, 18, -26, LOG)

# 斜め側面の障子
for z in [-18, -10, -2, 6, 14]:
    hw = half_width(z)

    # 左
    fill(-hw - 1, 16, z - 1, -hw - 1, 20, z + 1, PAPER)

    # 右
    fill(hw + 1, 16, z - 1, hw + 1, 20, z + 1, PAPER)

time.sleep(0.5)


# ------------------------------------------------------------
# 15. 下屋根
# ------------------------------------------------------------

# 正面の庇
fill(-14, 12, -29, 14, 12, -24, ROOF)
fill(-15, 11, -30, 15, 11, -30, ROOF_EDGE)

# V字に沿った下屋根
for z in range(-24, 19):
    hw = half_width(z)

    # 左側
    fill(-hw - 4, 12, z, -hw, 12, z, ROOF)
    setblock(-hw - 5, 11, z, ROOF_EDGE)

    # 右側
    fill(hw, 12, z, hw + 4, 12, z, ROOF)
    setblock(hw + 5, 11, z, ROOF_EDGE)

# 奥の庇
fill(-hw_back, 12, 18, hw_back, 12, 22, ROOF)
fill(-hw_back - 1, 11, 23, hw_back + 1, 11, 23, ROOF_EDGE)

time.sleep(0.5)


# ------------------------------------------------------------
# 16. 大屋根
# V字平面に合わせて、奥へ広がる屋根にする
# ------------------------------------------------------------

# 屋根レイヤー1
for z in range(-26, 21):
    hw = half_width(max(z, -24)) + 4
    fill(-hw, 22, z, hw, 22, z, ROOF)

# 屋根レイヤー2
for z in range(-23, 18):
    hw = half_width(max(z, -24)) + 1
    fill(-hw, 23, z, hw, 23, z, ROOF)

# 屋根レイヤー3
for z in range(-20, 15):
    hw = half_width(max(z, -24)) - 2
    fill(-hw, 24, z, hw, 24, z, ROOF)

# 屋根レイヤー4
for z in range(-17, 12):
    hw = half_width(max(z, -24)) - 5
    fill(-hw, 25, z, hw, 25, z, ROOF)

# 屋根レイヤー5
for z in range(-13, 8):
    hw = half_width(max(z, -24)) - 8
    fill(-hw, 26, z, hw, 26, z, ROOF)

# 屋根の縁取り
for z in range(-26, 21):
    hw = half_width(max(z, -24)) + 5
    setblock(-hw, 21, z, ROOF_EDGE)
    setblock(hw, 21, z, ROOF_EDGE)

fill(-16, 21, -27, 16, 21, -27, ROOF_EDGE)
fill(-28, 21, 21, 28, 21, 21, ROOF_EDGE)

time.sleep(0.5)


# ------------------------------------------------------------
# 17. 屋根上の小屋根
# ------------------------------------------------------------

# 小屋根の土台
fill(-8, 27, -4, 8, 27, 7, WOOD)
fill(-6, 28, -2, 6, 30, 5, WOOD)

# 小屋根
fill(-10, 31, -5, 10, 31, 8, ROOF)
fill(-8, 32, -3, 8, 32, 6, ROOF)
fill(-5, 33, -1, 5, 33, 4, ROOF)

# 屋根飾り
fill(0, 34, 0, 0, 37, 0, GOLD)
setblock(0, 38, 0, GOLD)

time.sleep(0.5)


# ------------------------------------------------------------
# 18. 右前の縦看板「百番」風
# 写真の右側に立つ大きな白看板の表現
# ------------------------------------------------------------

# 看板柱
fill(29, 1, -25, 29, 31, -25, LOG)

# 白看板
fill(30, 12, -26, 33, 30, -26, WHITE)

# 黒文字風
# 上の文字
fill(31, 26, -27, 32, 26, -27, BLACK)
fill(31, 27, -27, 31, 29, -27, BLACK)
fill(32, 25, -27, 32, 27, -27, BLACK)

# 中の文字
fill(31, 20, -27, 32, 20, -27, BLACK)
fill(31, 21, -27, 31, 23, -27, BLACK)
fill(32, 21, -27, 32, 23, -27, BLACK)
fill(31, 23, -27, 32, 23, -27, BLACK)

# 下の文字
fill(31, 15, -27, 32, 15, -27, BLACK)
fill(31, 16, -27, 31, 18, -27, BLACK)
fill(32, 16, -27, 32, 18, -27, BLACK)
fill(31, 18, -27, 32, 18, -27, BLACK)

# 看板の明かり
setblock(29, 13, -26, LAMP)
setblock(29, 30, -26, LAMP)

time.sleep(0.5)


# ------------------------------------------------------------
# 19. 正面・側面の夜景照明
# ------------------------------------------------------------

# 正面下部
for x in [-10, -5, 5, 10]:
    setblock(x, 4, -26, LAMP)

# V字側面下部
for z in [-20, -12, -4, 4, 12]:
    hw = half_width(z)
    setblock(-hw - 1, 4, z, LAMP)
    setblock(hw + 1, 4, z, LAMP)

# 周辺灯
for x, z in [(-18, -27), (18, -27), (-26, 5), (26, 5)]:
    fill(x, 1, z, x, 4, z, LOG)
    setblock(x, 5, z, LAMP)

time.sleep(0.5)


# ------------------------------------------------------------
# 20. 撮影用：斜め前から見る位置へ移動
# ------------------------------------------------------------
cmd("time set night")
# 右前から、V字の正面・右側・縦看板が見える想定
cmd("tp @p 48 24 -55 40 18")

print("鯛よし百番 V字平面版 完成")