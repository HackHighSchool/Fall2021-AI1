
import os

open_file = open("Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')
print(len(allTickers))

# '''
for i in range(0, 1024):
    if not os.path.exists(f"CSV_files/{allTickers[i]}"):
        print(f"Ticker {i}:{allTickers[i]} does not exist")
    else:
        if not os.path.exists(f"CSV_files/{allTickers[i]}/{allTickers[i]}_BalSheet.csv"):
            print(f"{allTickers[i]}_BalSheet.csv does not exist")
        if not os.path.exists(f"CSV_files/{allTickers[i]}/{allTickers[i]}_QuartBalSheet.csv"):
            print(f"{allTickers[i]}_QuartBalSheet.csv does not exist")
        if not os.path.exists(f"CSV_files/{allTickers[i]}/{allTickers[i]}_CashFlow.csv"):
            print(f"{allTickers[i]}_CashFlow.csv does not exist")
        if not os.path.exists(f"CSV_files/{allTickers[i]}/{allTickers[i]}_QuartCashFlow.csv"):
            print(f"{allTickers[i]}_QuartCashFlow.csv does not exist")
        if not os.path.exists(f"CSV_files/{allTickers[i]}/{allTickers[i]}_Earnings.csv"):
            print(f"{allTickers[i]}_Earnings.csv does not exist")
        if not os.path.exists(f"CSV_files/{allTickers[i]}/{allTickers[i]}_QuartEarnings.csv"):
            print(f"{allTickers[i]}_QuartEarnings.csv does not exist")
# '''
print("Finished!")
