import yfinance as yf
import pandas as pd

open_file = open("Russell1000Tickers.txt", "r")
requiredTickers = open_file.read().split('\n')
print(requiredTickers)

df_list = list()
for ticker in requiredTickers:
    data = yf.download(ticker.strip(), group_by="Ticker", period='max')
    data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
    df_list.append(data)

# combine all dataframes into a single dataframe
df = pd.concat(df_list)

# save to csv
df.to_csv('ticker.csv')