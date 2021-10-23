import yfinance as yf
import os

open_file = open("Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')
print(allTickers)

for i in range(0, 1024):
    TickerName = allTickers[i]
    print(TickerName)
    try:
        os.mkdir(f'CSV_files/{TickerName}')
    except FileExistsError:
        print(f'{TickerName} directory already exists.')
    ticker = yf.Ticker(TickerName)
    print("Data Retrieved...")
    ticker.balance_sheet.to_csv(f'CSV_files/{TickerName}/{TickerName}_BalSheet.csv')
    ticker.quarterly_balance_sheet.to_csv(f'CSV_files/{TickerName}/{TickerName}_QuartBalSheet.csv')
    ticker.cashflow.to_csv(f'CSV_files/{TickerName}/{TickerName}_CashFlow.csv')
    ticker.quarterly_cashflow.to_csv(f'CSV_files/{TickerName}/{TickerName}_QuartCashFlow.csv')
    ticker.earnings.to_csv(f'CSV_files/{TickerName}/{TickerName}_Earnings.csv')
    ticker.quarterly_earnings.to_csv(f'CSV_files/{TickerName}/{TickerName}_QuartEarnings.csv')
    print(f'.CSVs made. Ticker {i}: {TickerName} finished.')

open_file.close()
print("Done!")
