import pandas as pd
import numpy as np


from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score

#change for different tickers
TickerName ="AA"

data_file = "CSV_files/" + str(TickerName) + "/" + str(TickerName)+"_adjustedreturn.csv"
data = pd.read_csv(data_file)

#22 is replaced with the value that we are trying to predict so 22, 66, 132
y = data.AdjRet22Day
columns = ["Open","High", "Low", "Close", "Adj Close"]
X = data[columns]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

model = linear_model.LinearRegression()
model.fit(train_X,train_y)

predictions = model.predict(val_X)
print(predictions)
print(val_y)

#Mean Absolute Error
mae = mean_absolute_error(val_y, predictions)
print("Mean Absolute Error: " + str(mae))

#Root Mean Square Deviation
def rmse_cv(Model):
    rmse= np.sqrt(-cross_val_score(Model, train_X, train_y, scoring="neg_mean_squared_error", cv = 5))
    return(rmse)

print("Root Mean Square Error: " + str(rmse_cv(model).mean()))