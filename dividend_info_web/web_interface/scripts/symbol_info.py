import yfinance as yf
import pandas as pd

index='NS'

def get_company_info(symbol):
    print("Calling company info \n")
    try:
        ticker = yf.Ticker(f"{symbol}.{index}")
        print(f"Ticker : {ticker.ticker} \n\n")
        div_info = ticker.get_dividends()
        print(div_info)
        return ticker.get_dividends().to_dict()
    except Exception as e:
        return e

    