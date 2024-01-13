import pandas as pd

# 2つのCSVファイルを読み込む
df1 = pd.read_csv('output.csv')
df2 = pd.read_csv('in.csv')

# 2つのデータフレームを結合する
merged_df = pd.concat([df1, df2], axis=1)

# 結合したデータフレームをCSVファイルに保存する
merged_df.to_csv('tougou.csv', index=False, encoding='utf-8')