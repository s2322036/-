import sqlite3
import requests
from bs4 import BeautifulSoup
import time

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
sql_create_table_weather = 'CREATE TABLE weather(temperature int, humidity int);'
# 4．SQLを実行する
cur.execute(sql_create_table_weather)
# 5．必要があればコミットする（データ変更等があった場合）
# 今回は必要なし
# 6．DBへの接続を閉じる
con.close()

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=45&block_no=47682&year=2024&month=1&day=12&view='
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)
soup.find_all(attrs={'class': 'mtx'})

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=45&block_no=47682&year=2024&month=1&day=12&view='
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)
# Find all elements with class 'mtx'
elements_with_class_mtx = soup.find_all(attrs={'class': 'mtx'})
# Extract and print the text content from each element
for element in elements_with_class_mtx:
    text = element.get_text(strip=True)
    print(text)

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=45&block_no=47682&year=2024&month=1&day=12&view='
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)
# Find all elements with class 'mtx'
elements_with_class_mtx = soup.find_all(attrs={'class': 'mtx'})
# Extract and print the temperature data from the third column
for element in elements_with_class_mtx:
    columns = element.find_all('td')
    if len(columns) >= 3:  # Check if there are at least three columns
        temperature_data = columns[4].get_text(strip=True)
        print("気温:", temperature_data)

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=45&block_no=47682&year=2024&month=1&day=12&view='
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)
# Find all elements with class 'mtx'
elements_with_class_mtx = soup.find_all(attrs={'class': 'mtx'})
# Extract and print the temperature data from the third column
for element in elements_with_class_mtx:
    columns = element.find_all('td')
    if len(columns) >= 3:  # Check if there are at least three columns
        humidity_data = columns[7].get_text(strip=True)
        print("湿度:", humidity_data)

        import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/hourly_s1.php?prec_no=45&block_no=47682&year=2024&month=1&day=12&view='
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")
time.sleep(1)
# Find all elements with class 'mtx'
elements_with_class_mtx = soup.find_all(attrs={'class': 'mtx'})
# Data list to store temperature and humidity pairs
temperature_humidity_data_list = []
# Extract and append temperature and humidity data from the fourth and eighth columns, respectively
for element in elements_with_class_mtx:
    columns = element.find_all('td')
    if len(columns) >= 8:  # Check if there are at least eight columns
        temperature_data = columns[4].get_text(strip=True)
        humidity_data = columns[7].get_text(strip=True)
        temperature_humidity_data_list.append((temperature_data, humidity_data))
# Display the extracted temperature and humidity data list
print("気温と湿度データリスト:", temperature_humidity_data_list)

# 例として、文字列から浮動小数点数に変換する
temperature = float(temperature_data)
humidity = float(humidity_data)
# データベースへの接続
con = sqlite3.connect("dsprogramming.db")
c = con.cursor()
# データベースに挿入
c.execute("INSERT INTO weather(temperature, humidity) VALUES (?, ?)", (temperature, humidity))
con.commit()
# データベースのコネクションを閉じる
con.close()

import sqlite3
# データベースへの接続
con = sqlite3.connect("dsprogramming.db")
c = con.cursor()
# データの取得とデータベースへの挿入
for temperature, humidity in temperature_humidity_data_list:
    # 例として、文字列から浮動小数点数に変換する
    temperature = float(temperature)
    humidity = float(humidity)
    # データベースに挿入
    c.execute("INSERT INTO weather(temperature, humidity) VALUES (?, ?)", (temperature, humidity))
# データベースへの変更をコミット
con.commit()
# データベースのコネクションを閉じる
con.close()



import sqlite3
import csv

# データベースへの接続
con = sqlite3.connect("dsprogramming.db")
c = con.cursor()

# データベースからデータを取得
c.execute("SELECT temperature, humidity FROM weather")
data = c.fetchall()

# データベースのコネクションを閉じる
con.close()