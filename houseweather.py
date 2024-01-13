import sqlite3

# DBファイルを保存するためのファイルパス
# Google Colab
path = '/Users/riontakano/-/'
# ローカル（自分のMac）
# path = '../db/'
# DBファイル名
db_name = 'dsprogramming.db'
# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect(path + db_name)
c = con.cursor()
# DBへの接続を閉じる
con.close()

# 1．DBに接続する
con = sqlite3.connect(path + db_name)
# print(type(con))
# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()
# 3．実行したいSQLを用意する
# テーブルを作成するSQL
# CREATE TABLE テーブル名（カラム名 型，...）;
sql_create_table_houseweather = 'CREATE TABLE houseweather(temperature int, humidity int);'
# 4．SQLを実行する
cur.execute(sql_create_table_houseweather)
# 5．必要があればコミットする（データ変更等があった場合）
# 今回は必要なし
# 6．DBへの接続を閉じる
con.close()

import sqlite3
# 1．データベースに接続
con = sqlite3.connect("dsprogramming.db")
cur = con.cursor()
# 2．テーブルの作成
sql_create_table = """
CREATE TABLE IF NOT EXISTS houseweather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity INTEGER
);
"""
cur.execute(sql_create_table)
# 3．データの挿入
sql_insert = "INSERT INTO houseweather (temperature, humidity) VALUES (?, ?)"
# 4．データのリスト
houseweather_list = [
    (1.2, 64),
    (0.8, 66),  # humidityの値を入れてください
    (0.1, 70),
    (-0.6, 74),
    (0.2, 68),
    (-0.3, 71),
    (-0.6, 71),
    (1.1, 64),
    (4.2, 59),
    (7.9, 50),
    (11.1, 41),
    (13.0, 38),
    (13.9, 38),
    (14.8, 41),
    (14.2, 43),
    (13.3, 48),
    (10.0, 62),
    (7.0, 74),
    (5.0, 81),
    (4.8, 83),
    (6.7, 75),
    (6.1, 69),
    (3.5, 81),
    (5.5, 61),
]
# 5．SQLを実行
cur.executemany(sql_insert, houseweather_list)
# 6．コミット処理（データ操作を反映させる）
con.commit()
# 7．データベースのコネクションを閉じる
con.close()

import sqlite3
# データベースへの接続
con = sqlite3.connect("dsprogramming.db")
c = con.cursor()
    # データベースに挿入
"INSERT INTO weather(temperature, humidity) VALUES (?, ?)"
# データベースへの変更をコミット
con.commit()
# データベースのコネクションを閉じる
con.close()