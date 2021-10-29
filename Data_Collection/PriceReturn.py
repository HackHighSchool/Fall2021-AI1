import yfinance as yf
import pandas as pd

open_file = open("Russell1000Tickers.txt", "r")
allTickers = open_file.read().split('\n')
daysahead = [22, 66, 132]

for i in range(0, 1024):
    try:
        TickerName = allTickers[i]
        CSV_file = "CSV_files/"+str(TickerName)+"/"+str(TickerName)+"_price.csv"
        data = pd.read_csv(CSV_file)
        NewCSV_file = "CSV_files/" + str(TickerName) + "/" + str(TickerName)+"_pricedepvar.csv"
        for j in daysahead:
            PriceReturn=[]
            for row in range(len(data)-j):
                PriceReturn.append(data["Adj Close"][row+j]/data["Adj Close"][row])
            for row in range(len(data)-j, len(data)):
                PriceReturn.append(0)
            data["PriceReturn_"+str(j)+"days"]=PriceReturn
            data.to_csv(NewCSV_file, index=False)
    except:
        print("Could not find file for "+allTickers[i])