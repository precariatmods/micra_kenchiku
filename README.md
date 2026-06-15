# Minecraft Python 建築

Minecraft を Python で自動建築するサンプル集です。

## 動画
YouTube ショートで公開中

## 動作環境
- Python 3.10.11
- java version "25.0.3" 2026-04-21 LTS
- Paper Server
- Geyser-Spigot
- floodgate-spigot
- RCON (pip install mctools) で導入

## 概要

Python から RCON を利用して Minecraft に建築コマンドを送信しています。

建築物は座標 (0, 0, 0) を中心として作成していますので、実行前に整地してください。

以下の整地プログラムを利用しています。

X方向 ±200
Z方向 ±200
高さ Y=100 までを空間化
地面をシーランタンブロックで作成

整地プログラム

https://github.com/precariatmods/micra_kenchiku/blob/main/seichi.py

## 特徴

- 各サンプルは1ファイルで実行可能
- Python から RCON を利用して Minecraft を操作
- マインクラフト教育用教材として作成



## サンプル一覧

| ファイル | 内容 |
|----------|------|
| seichi.py | 整地プログラム |
| roudou.py | 労働センター建築 |
| aizendo.py | 愛染堂建築 |
