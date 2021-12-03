import pandas as pd

from sklearn.linear_model import LassoCV
from sklearn.model_selection import train_test_split
from scipy import stats

open_file = open("Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')

results =[]

commonColumns = ["Total Liab", "Total Stockholder Equity", "Total Assets", "Cash", "Total Current Liabilities", "Total Current Assets", "Net Tangible Assets", "Change To Liabilities", "Total Cashflows From Investing Activities", "Total Cash From Financing Activities", "Net Income", "Change In Cash", "Total Cash From Operating Activities", "Change To Netincome"]
first = True

for t in range(0, 1024):
    try:
        TickerName = allTickers[t]

        data_file = "CSV_files/" + str(TickerName) + "/" + str(TickerName)+"_CombinedFiles.csv"
        data = pd.read_csv(data_file)
        data = data[commonColumns + ["AdjRet22Day"]]
        data = data.dropna(axis=0)

        print(t)
        y = data.AdjRet22Day

        X = data[commonColumns]
        if first:
            combinedX = X
            combinedy = y
            first = False
        else:
            combinedX = combinedX.append(X)
            combinedy = combinedy.append(y)

    except:
        print("Could not find file for "+ allTickers[t] + " or there was a column of missing values")

combinedX = pd.DataFrame(stats.zscore(combinedX,axis=0),columns=combinedX.columns)

train_X, val_X, train_y, val_y = train_test_split(combinedX, combinedy)

model = LassoCV(alphas = [1, 0.1, 0.001, 0.0005]).fit(train_X, train_y)

predictions = model.predict(val_X)


#Hit Rate Validation
hitrate = 0
indexes = val_y.index.values
index_list = list(indexes)
n = 0
for x in predictions:
    if x < 0 and val_y.iloc[n] < 0:
        hitrate += 1
        n += 1
    elif x > 0 and val_y.iloc[n]> 0:
        hitrate += 1
        n += 1
    else:
        n += 1

hitrate = hitrate/len(index_list)
print("Hit Rate: " + str(hitrate))

