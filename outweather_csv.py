import sqlite3
import csv

# データベースに接続
conn = sqlite3.connect('dsprogramming.db')
cursor = conn.cursor()

# データの取得（例：テーブル名が 'your_table'）
cursor.execute('SELECT * FROM weather')
data = cursor.fetchall()

# CSVに変換
with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description])  # ヘッダー行を追加
    csv_writer.writerows(data)

# データベースとの接続を閉じる
conn.close()