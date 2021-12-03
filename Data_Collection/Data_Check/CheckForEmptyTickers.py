# Spacer

import pandas as pd

open_file = open("../Assisting_files/Russell1000Tickers.txt")
tickers = open_file.read().splitlines()
open_file.close()
types = ("", "Quart")
emptyTickers = []
for ticker in tickers:
    for fileType in types:
        fileCheck = pd.read_csv(f"CSV_files/{ticker}/{ticker}_{fileType}BalSheet+{fileType}CashFlow.csv")
        if not fileCheck.values.any():
            emptyTickers.append(ticker)
            print(ticker)
            break
open_file = open("../Assisting_files/EmptyTickers.txt", "w")
for i in emptyTickers:
    open_file.write(i + "\n")
open_file.close()

