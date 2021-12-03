import pandas as pd

# Spacer


open_file = open("../Assisting_files/Russell1000Tickers.txt")
tickerList = open_file.read().splitlines()
open_file.close()
open_file = open("../Assisting_files/EmptyTickers.txt")
emptyTickers = open_file.read().splitlines()
open_file.close()
sheetTypeList = ("", "Quart")
ColumnsShared = list(pd.read_csv(f"../CSV_files/A/A_BalSheet+CashFlow.csv").iloc[:, 0])
print(ColumnsShared)
print("Start:\n")

for tick in range(0, 1024):
    ticker = tickerList[tick]
    if ticker in emptyTickers:
        continue
    for sheetType in sheetTypeList:
        df1 = pd.read_csv(f"CSV_files/{ticker}/{ticker}_{sheetType}BalSheet+{sheetType}CashFlow.csv")
        # print(df1)
        if True:
            for indexName in ColumnsShared:
                # print(indexName)
                if indexName not in list(df1.iloc[:, 0]):
                    print(f"Index removed:{indexName}")
                    ColumnsShared.remove(indexName)
    print(f"\nFinished Ticker {tick + 1}.\nNext Ticker: {tick + 2}")
    # print(ColumnsShared)
open_file = open("../Assisting_files/Shared_Columns.txt", "w")
print(ColumnsShared)
for i in ColumnsShared:
    open_file.write(i + "\n")
