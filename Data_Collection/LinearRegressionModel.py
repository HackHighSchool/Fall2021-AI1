import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics
import statsmodels.api as sm

# load dataset
df = pd.read_csv('C:\\ProgramData\\cjccl\\GitHubDesktop\\app-2.9.4\\Fall2021-AI1\\Data_Collection\\CSV_files\\AMZN\\AMZN_CombinedFiles.csv')

#print(df.to_string())

#df = pd.DataFrame(dataframe, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'ticker', 'PriceReturn'])

X = df[['AdjRet22Day']]
Y = df['PriceReturn_22days']

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.1,
                                                    random_state=1)

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, Y_train)

# regression coefficients
print('Coefficients: ', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, Y_test)))

# plot for residual error

## setting plot style
plt.style.use('fivethirtyeight')

## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - Y_train,
            color="green", s=1, label='Train data')

## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - Y_test,
            color="blue", s=1, label='Test data')

## plotting line for zero residual error
plt.hlines(y=0, xmin=0, xmax=2, linewidth=2)

## plotting legend
plt.legend(loc='upper right')

## plot title
plt.title("Residual errors")

## method call for showing the plot
#plt.show()


print('Train Score: ', reg.score(X_train, Y_train))
print('Test Score: ', reg.score(X_test, Y_test))

print('Intercept: \n', reg.intercept_)
print('Coefficients: \n', reg.coef_)

X = sm.add_constant(X)  # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)