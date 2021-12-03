import pandas as pd
import sys

base_dir="C:/Users/admin/Documents/GitHub/Fall2021-AI1/Data_Collection/CSV_files/"
from_date="2017-09-29"

# FIXME - these tickers are excluded bcoz the CSV files are missing PriceReturn columns
excludedtickers = [] #['ALXN', 'BPYU', 'XEC', 'FICO', 'LB', 'ODFL', 'PLTR', 'PRAH', 'PWR', 'WORK', 'VMEO', 'UDR', 'WRI', 'A', 'DV', 'OGN']

# read all tickers
tickers_file=open(base_dir + "../Russell1000Tickers.txt", "r")
tickers = tickers_file.read().split('\n')

# read one ticker to fetch dates, column
df = pd.read_csv(base_dir + "AAPL/AAPL_pricedepvar.csv")
df = df[df['Date'] >= from_date]

# master dataframe will hold all the values
master_df = pd.DataFrame(columns=['Date', 'ticker', 'PriceReturn_22days', 'PriceReturn_66days','PriceReturn_132days'])

# open all csvs
print("Loading all tickers...")

for t in tickers:

    if not t in excludedtickers:
        try:
            #print("Loading " + t)
            x = pd.read_csv(base_dir + str(t) + "/" + str(t) + "_pricedepvar.csv", usecols=['Date', 'PriceReturn_22days', 'PriceReturn_66days', 'PriceReturn_132days'])
            x["ticker"] = t
            # filter non-zero values
            x = x[x['PriceReturn_22days'] != 0]
            x = x[x['PriceReturn_66days'] != 0]
            x = x[x['PriceReturn_132days'] != 0]
            x = x[x['Date'] >= from_date]
        except:
            print("Error loading CSV for ticker " + t)
            e = sys.exc_info()[0]
            print(str(e))

    master_df = master_df.append(x)


master_df.set_index(['Date', 'ticker'])

# create a new column in dataframe to hold price return difference

# Calculate means by date
means = master_df.groupby('Date')['PriceReturn_22days'].mean()
means66 = master_df.groupby('Date')['PriceReturn_66days'].mean()
means132 = master_df.groupby('Date')['PriceReturn_132days'].mean()



# for every date, subtract the price return from mean
#for i in range(1006):
for t in tickers:
    #t = tickers[i]
    CSV_file = "CSV_files/" + str(t) + "/" + str(t) + "_pricedepvar.csv"
    if not t in excludedtickers:
        #print('ticker is ' + t)
        data = pd.read_csv(CSV_file)
        try:
            merged = data.merge(means.to_frame(),left_on='Date',right_on='Date',suffixes=['','_mean'])
            merged2 = data.merge(means66.to_frame(), left_on='Date', right_on = 'Date',suffixes=['','_mean'])
            merged3 = data.merge(means132.to_frame(), left_on='Date', right_on = 'Date',suffixes=['','_mean'])

            merged['AdjRet22Day'] = merged['PriceReturn_22days'] - merged['PriceReturn_22days_mean']
            merged['AdjRet66Day'] = merged2['PriceReturn_66days']- merged2['PriceReturn_66days_mean']
            merged['AdjRet132Day'] = merged3['PriceReturn_132days'] - merged3['PriceReturn_132days_mean']
            Newfile = "CSV_files/" + str(t) + "/" + str(t)+"_adjustedreturn.csv"
            merged.to_csv(Newfile, index=False)
        except:
            print("Error merging data for ticker " + t)
            e = sys.exc_info()[0]
            print(str(e))











