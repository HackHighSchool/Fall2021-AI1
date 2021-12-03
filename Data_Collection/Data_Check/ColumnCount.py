import pandas as pd

open_file = open("../Assisting_files/Russell1000Tickers.txt", "r")
tickers = open_file.read().split("\n")
open_file.close()

columnCount = {}

open_file = open("../Assisting_files/EmptyTickers.txt", "r")
empty = open_file.read().split("\n")
open_file.close()

for i in range(len(tickers)):
    ticker = tickers[i]
    if ticker in empty:
        continue
    print(f"ticker {i}: {ticker}")
    df1 = pd.read_csv(f"../CSV_files/{ticker}/{ticker}_BalSheet+CashFlow.csv", index_col=0)
    for column in df1.index:
        if column in columnCount.keys():
            columnCount[column] += 1
        else:
            columnCount[column] = 1
print(columnCount)

counts = pd.DataFrame(list(columnCount.items()), columns=["Column Names", "Column Counts"])
print(counts)
counts.to_csv("../Assisting_files/columnCount.csv")
# counts.to_csv("C:/Users/Kenny Leeper/OneDrive/Documents/GitHub/Fall2021-AI1/Data_Collection/Assisting_files/columnCount.csv")
