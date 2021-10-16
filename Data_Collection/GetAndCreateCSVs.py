
import yfinance as yf
import shutil
import os

open_file = open("Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')
print(allTickers)

for i in range(512, 769):
    TickerName = allTickers[i]
    print(TickerName)
    try:
        os.mkdir(f'CSV_files/{TickerName}')
    except FileExistsError:
        print(f'{TickerName} directory already exists.')
    ticker = yf.Ticker(TickerName)
    print("Data Retrieved...")
    ticker.balance_sheet.to_csv(f'{TickerName}_BalSheet.csv')
    ticker.quarterly_balance_sheet.to_csv(f'{TickerName}_QuartBalSheet.csv')
    ticker.cashflow.to_csv(f'{TickerName}_CashFlow.csv')
    ticker.quarterly_cashflow.to_csv(f'{TickerName}_QuartCashFlow.csv')
    ticker.earnings.to_csv(f'{TickerName}_Earnings.csv')
    ticker.quarterly_earnings.to_csv(f'{TickerName}_QuartEarnings.csv')
    print(".CSVs made...")
    shutil.move(f'{TickerName}_BalSheet.csv', f'CSV_files/{TickerName}')
    shutil.move(f'{TickerName}_QuartBalSheet.csv', F"CSV_files/{TickerName}")
    shutil.move(f'{TickerName}_CashFlow.csv', f"CSV_files/{TickerName}")
    shutil.move(f'{TickerName}_QuartCashFlow.csv', f"CSV_files/{TickerName}")
    shutil.move(f'{TickerName}_Earnings.csv', f"CSV_files/{TickerName}")
    shutil.move(f'{TickerName}_QuartEarnings.csv', f"CSV_files/{TickerName}")
    print(f'Moved Files. Finished ticker {i}')

open_file.close()
print("Done!")
