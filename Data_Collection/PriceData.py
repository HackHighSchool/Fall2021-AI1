import yfinance as yf
import os

open_file = open("Russell1000Tickers.txt", "r")
requiredTickers = open_file.read().split('\n')
print(requiredTickers)

for ticker in requiredTickers:
    data = yf.download(ticker.strip(), group_by="Ticker", period='max')
    try:
        os.mkdir(f'CSV_files/{ticker}')
    except FileExistsError:
        print(f'{ticker} directory already exists.')
    data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
    # save to csv
    data.to_csv('CSV_files/' + ticker + '/price.csv')

