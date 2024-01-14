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
sql_create_table_houseweather = 'CREATE TABLE houseweather(temperature_house int, humidity_house int);'
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
    temperature_house REAL,
    humidity_house INTEGER
);
"""
cur.execute(sql_create_table)
# 3．データの挿入
sql_insert = "INSERT INTO houseweather (temperature_house, humidity_house) VALUES (?, ?)"
# 4．データのリスト
houseweather_list = [
    (1.2, 62),
    (1.0, 69),  # humidity_houseの値を入れてください
    (0.2, 70),
    (-0.4, 76),
    (0.3, 67),
    (-0.4, 68),
    (-0.5, 73),
    (1.0, 65),
    (4.6, 59),
    (7.9, 52),
    (11.7, 43),
    (13.5, 32),
    (14.2, 40),
    (15.3, 42),
    (14.2, 45),
    (13.6, 48),
    (10.8, 66),
    (6.8, 71),
    (5.0, 81),
    (4.9, 85),
    (7.0, 78),
    (6.5, 63),
    (3.2, 79),
    (5.5, 62),
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
"INSERT INTO weather(temperature_house, humidity_house) VALUES (?, ?)"
# データベースへの変更をコミット
con.commit()
# データベースのコネクションを閉じる
con.close()