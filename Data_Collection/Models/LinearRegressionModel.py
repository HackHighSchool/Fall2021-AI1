import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
import statsmodels.api as sm
from scipy import stats
import glob

open_file = open("Russell1000Tickers.txt", "r")
requiredTickers = open_file.read().split('\n')

open_file = open("EmptyTickers.txt", "r")
emptyTickers = open_file.read().split('\n')

open_file = open("Shared_Columns.txt", "r")
sharedColumns = open_file.read().split('\n')

# load dataset
base_dir = "C:/ProgramData/cjccl/GitHubDesktop/app-2.9.4/Fall2021-AI1/Data_Collection/CSV_files"
all_files = []
for ticker in requiredTickers:
    if ticker not in emptyTickers:
        all_files.append(base_dir + f'/{ticker}/{ticker}_CombinedFiles.csv')

first = True

totalDf = []

for file in all_files[:250]:
    df = pd.read_csv(file, index_col=None, header=0)
    #print(file)

    if first:
        totalDf = df
        first = False
    else:
        totalDf = totalDf.append(df)
currDf = totalDf
for column in totalDf:
   if column not in sharedColumns:
       #print(column)
       currDf = currDf.drop(column, axis = 1)
   else:
       totalDf = totalDf.dropna(subset=[column])

currDf = currDf.dropna()

X = pd.DataFrame(stats.zscore(currDf,axis=0),columns=currDf.columns)
y = totalDf['AdjRet22Day']
#splitting X and Y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state=42)

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

print('Train Score: ', reg.score(X_train, y_train))
print('Test Score: ', reg.score(X_test, y_test))

print('Intercept: \n', reg.intercept_)
print('Coefficients: \n', reg.coef_)

# OLS Method
X = sm.add_constant(X)  # adding a constant

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)

print('Variance score: {}'.format(reg.score(X_test, y_test)))

# plot for residual error

## setting plot style
plt.style.use('fivethirtyeight')

## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
            color="green", s=1, label='Train data')

## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
            color="blue", s=0.01, label='Test data')

## plotting line for zero residual error
plt.hlines(y=0, xmin=-0.2, xmax=0.2, linewidth=0.1)

## plotting legend
plt.legend(loc='upper right')

## plot title
plt.title("Residual errors")

## method call for showing the plot
plt.show()

