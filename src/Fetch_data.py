import pandas as pd
import yfinance as yf
import os

file_path = '/Users/gowtham/Desktop/Project_Stocks/config/tickers.csv'

tickers = pd.read_csv(file_path)

tickers = tickers['Ticker'].dropna().tolist()
#print(tickers)

os.makedirs('/Users/gowtham/Desktop/Project_Stocks/data', exist_ok= True)

for ticker in tickers:
    print(f"fetching {ticker} ticker")
    stock = yf.Ticker(ticker)
    hist = stock.history(period = '15d')


    if not hist.empty:
        hist.to_csv(f'/Users/gowtham/Desktop/Project_Stocks/data/{ticker}.csv')
    else:
        print(f'No data found for {ticker} ticker')
