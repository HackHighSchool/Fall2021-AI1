import pandas as pd
from scipy import stats

from sklearn import linear_model
from sklearn.model_selection import train_test_split

open_file = open("../Assisting_files/Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')

commonColumns = ["Close","Total Liab", "Total Stockholder Equity", "Total Assets", "Cash", "Total Current Liabilities", "Total Current Assets", "Net Tangible Assets", "Change To Liabilities", "Total Cashflows From Investing Activities", "Total Cash From Financing Activities", "Net Income", "Change In Cash", "Total Cash From Operating Activities", "Change To Netincome"]
first = True

results =[]

for t in range(0, 1024):
    try:
        TickerName = allTickers[t]

        data_file = "../CSV_files/" + str(TickerName) + "/" + str(TickerName)+"_CombinedFiles.csv"
        data = pd.read_csv(data_file)
        data = data[commonColumns + ["AdjRet132Day"]]
        data = data.dropna(axis=0)

        print(t)
        y = data.AdjRet132Day

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

model = linear_model.LinearRegression()
model.fit(train_X,train_y)

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

hitrate = hitrate/(len(index_list)+0.0)
print("Hit Rate: " + str(hitrate))
