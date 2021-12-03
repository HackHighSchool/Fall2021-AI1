import pandas as pd
import numpy as np
import csv

from sklearn.linear_model import LassoCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score

open_file = open("Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')

results =[]

for t in range(0, 250):
    try:
        TickerName = allTickers[t]

        data_file = "CSV_files/" + str(TickerName) + "/" + str(TickerName)+"_CombinedFiles.csv"
        data = pd.read_csv(data_file)

        data = data.dropna()


#22 is replaced with the value that we are trying to predict so 22, 66, 132
        y = data.AdjRet22Day
        columns = list(data.columns)
        remove = ["ticker", "Date", "PriceReturn_22days", "PriceReturn_66days", "PriceReturn_132days", "PriceReturn_22days_mean","AdjRet22Day", "AdjRet66Day","AdjRet132Day"]
        for i in remove:
            columns.remove(i)
#use columns.txt later
        X = data[columns]

        train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

        model = LassoCV(alphas = [1, 0.1, 0.001, 0.0005]).fit(train_X, train_y)

        predictions = model.predict(val_X)
        #print(predictions)
        #print(val_y)

#Hit Rate Validation
        hitrate = 0
        indexes = val_y.index.values
        index_list = list(indexes)
        #print(index_list)
        n = 0
        for x in predictions:
            #print(x)
            index = index_list[n]
            #print(val_y[index])
            if x < 0 and val_y[index] < 0:
                hitrate += 1
                n += 1
            elif x > 0 and val_y[index]> 0:
                hitrate += 1
                n += 1
            else:
                n += 1

        hitrate = hitrate/len(index_list)
        #print("Hit Rate: " + str(hitrate))

        results.append([str(TickerName), str(hitrate)])
        #print(results)

    except:
        print("Could not find file for "+ allTickers[t])

#creating CSV to store data
header = ["Ticker", "Hit Rate"]

with open("Hit rates/LassoHitRates_dc", "w", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results)