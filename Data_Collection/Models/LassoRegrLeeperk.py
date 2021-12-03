import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.linear_model import RidgeCV, LassoCV

open_file = open("../Assisting_files/EmptyTickers.txt")
empty = open_file.read().split("\n")
open_file.close()

open_file = open("../Assisting_files/Russell1000Tickers.txt")
tickers = open_file.read().split("\n")
open_file.close()

first = True
for i in range(0,250):
    if tickers[i] in empty:
        continue
    if first:
        data = pd.read_csv(f"CSV_files/{tickers[i]}/{tickers[i]}_CombinedFiles.csv")
        first = False
        continue

    df1 = pd.read_csv(f"CSV_files/{tickers[i]}/{tickers[i]}_CombinedFiles.csv")
    data = pd.concat([data, df1], ignore_index=True, join="inner")
    print(f"ticker {i} completed: {tickers[i]}")
print(data)


open_file = open("../Assisting_files/Shared_Columns.txt")
sharedColumns = open_file.read().split("\n")
open_file.close()
temp1 = []

# Only use Shared Columns
for i in range(list(data.columns).index("AdjRet132Day") + 1, len(data.columns)):
    if data.columns[i] not in sharedColumns:
        temp1.append(data.columns[i])
data = data.drop(temp1, axis=1)

print(data)
print(data["AdjRet22Day"])

# data = data.drop("Repurchase Of Stock", axis=1)
# data = data.dropna(axis=1, how="any")

data = data.dropna()

y = data["AdjRet22Day"]

currData = data.drop(['AdjRet132Day', 'AdjRet66Day', 'AdjRet22Day', 'PriceReturn_22days_mean', 'PriceReturn_22days',
                      'PriceReturn_66days', 'PriceReturn_132days', 'Date', 'ticker'], axis=1)

# currData = currData + np.random.normal(0, .5, [currData.shape[0], currData.shape[1]])

x = pd.DataFrame(stats.zscore(currData, axis=0), columns=currData.columns)

print("\nIndependent Values:")
print(x)

print("\nDependent Values:")
print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=1)

print(X_train)
print(y_train)
lasso_model = Lasso().fit(X_train, y_train)


# Coefficients for different lambda values.

lasso = Lasso()
coefs = []
alphas = np.random.randint(0, 1000, 100)

# 10**np.linspace(10,-2,100)*0.5 -- It can be used instead of alphas and observed.

for a in alphas:
    lasso.set_params(alpha=a)
    lasso.fit(X_train, y_train)
    coefs.append(lasso.coef_)

ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale("log")


y_pred = lasso_model.predict(X_test)
print(y_pred)
errorVal = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R2 Score: {r2_score(y_test, y_pred)}")
print(f"RMSE: {errorVal}")
print(lasso_model.coef_)
print(f"\n{pd.Series(lasso_model.coef_, index = X_train.columns)}\n\n")

print("CV Lasso:")
lasso_cv_model = LassoCV(alphas=np.random.randint(0, 1000, 100), cv=10, max_iter=100000).fit(X_train, y_train)

lasso_tuned = Lasso().set_params(alpha = lasso_cv_model.alpha_).fit(X_train,y_train)

y_pred_tuned = lasso_tuned.predict(X_test)

CVErrorVal = np.sqrt(mean_squared_error(y_test,y_pred_tuned))
print(CVErrorVal)
print(f"\n{pd.Series(lasso_tuned.coef_, index = X_train.columns)}")

