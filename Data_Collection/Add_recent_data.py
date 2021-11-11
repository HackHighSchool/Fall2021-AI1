import pandas as pd

# Spacer

def grab_date(date: str):
    global year
    global month
    global day
    global dateComb
    year = date[0:4]
    month = date[5:7]
    day = date[8:]
    dateComb = year + month + day


open_file = open("Russell1000Tickers.txt")
tickerList = open_file.read().splitlines()
open_file.close()
open_file = open("EmptyTickers.txt")
emptyTickers = open_file.read().splitlines()
open_file.close()
year: str = ''
month: str = ''
day: str = ''
dateComb = ''
sheetTypeList = ("", "Quart")
# ColumnsShared = list(pd.read_csv(f"CSV_files/A/A_BalSheet+CashFlow.csv").iloc[:, 0])
# print(ColumnsShared)

#  ALXN, ticker 32, has no data
for tick in range(0, 1024):
    ticker = tickerList[tick]
    if ticker in emptyTickers:
        continue
    for sheetType in sheetTypeList:
        priceSheet = pd.read_csv(f"CSV_files/{ticker}/{ticker}_pricedepvar.csv", index_col=0)
        # print(priceSheet)
        df1 = pd.read_csv(f"CSV_files/{ticker}/{ticker}_{sheetType}BalSheet+{sheetType}CashFlow.csv", index_col=0)
        # print(df1)
        # if tick != 0:
        #     for indexName in ColumnsShared:
        #         if indexName not in list(df1.iloc[:, 0]):
        #             ColumnsShared.remove(indexName)
        df1 = df1.transpose()
        for i in range(0, len(priceSheet)):
            grab_date(df1.index[-1])
            dateCombSave = dateComb
            grab_date(priceSheet.index[i])
            if dateComb >= dateCombSave:
                break
        else:
            print("No Available Data")
        if not (i == len(priceSheet) - 1):
            df1Index = (len(df1) - 1)
            dfConcat = pd.DataFrame(index=[f"{year}-{month}-{day}"], columns=df1.columns.values.tolist())
            for j in range(i, len(priceSheet)):
                if df1Index != 0:
                    grab_date(df1.index[df1Index - 1])
                else:
                    grab_date(df1.index[df1Index])
                dateCombSave = dateComb
                grab_date(priceSheet.index[j])
                if (dateComb >= dateCombSave) and (df1Index != 0):
                    df1Index -= 1
                grab_date(df1.index[df1Index])
                dfConcat.loc[priceSheet.index[j]] = df1.loc[f"{year}-{month}-{day}"]
            dfFinal = priceSheet.join(dfConcat)
            dfFinal.fillna(method="backfill")
            if sheetType == "":
                print(f'Ticker finished: {ticker}:{tick}. type:normal')
            else:
                print(f'Ticker finished: {ticker}:{tick}. type:{sheetType}')
            dfFinal.to_csv(f"CSV_files/{ticker}/{ticker}_{sheetType}CombinedFiles.csv")
# open_file = open("Shared_Columns.txt", "w")
# print(ColumnsShared)
# for i in ColumnsShared:
#     open_file.write(i + "\n")
