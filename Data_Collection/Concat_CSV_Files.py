import pandas as pd
#import numpy as np
open_file = open("Russell1000Tickers.txt")
tickers = open_file.read().split("\n")
print(tickers)
for i in range(0, 1024):
    ticker = tickers[i]
    csv1 = pd.read_csv(f"CSV_files/{ticker}/{ticker}_BalSheet.csv")
    csv2 = pd.read_csv(f"CSV_files/{ticker}/{ticker}_CashFlow.csv")

    csv3 = pd.read_csv(f"CSV_files/{ticker}/{ticker}_QuartBalSheet.csv")
    csv4 = pd.read_csv(f"CSV_files/{ticker}/{ticker}_QuartCashFlow.csv")

    print("Read Files...")
    tickerGrouping = [csv1, csv2]
    fileMake = open(f"CSV_files/{ticker}/{ticker}_BalSheet+CashFlow.csv", "w")
    fileMake.write(pd.DataFrame.to_csv(pd.concat(tickerGrouping)))
    fileMake.close()
    print("First Done...")
    tickerGrouping = [csv3, csv4]
    fileMake = open(f"CSV_files/{ticker}/{ticker}_QuartBalSheet+QuartCashFlow.csv", "w")
    fileMake.write(pd.DataFrame.to_csv(pd.concat(tickerGrouping)))
    fileMake.close()
    print(f"Finished both files. Ticker finished: {ticker}")