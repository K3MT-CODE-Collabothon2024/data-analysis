import yfinance as yf

def fetch_stock_data(ticker, interval, period):
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.history(interval=interval, period=period)

        data = []
        for index, row in stock_info.iterrows():
            data.append({
                "ticker": ticker.upper(),
                "date": index.strftime('%Y-%m-%d'),
                "open": float(row['Open']),
                "close": float(row['Close']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "volume": int(row['Volume']),
            })

        return data

    except Exception as e:
        return {"error": str(e)}

import yfinance as yf

def fetch_currency_data(currency_pair, interval, period):
    try:
        currency = yf.Ticker(currency_pair)
        currency_info = currency.history(interval=interval, period=period)

        data = []
        for index, row in currency_info.iterrows():
            data.append({
                "currency_pair": currency_pair.upper(),
                "date": index.strftime('%Y-%m-%d'),
                "open": float(row['Open']),
                "close": float(row['Close']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "volume": int(row['Volume']),
            })

        return data

    except Exception as e:
        return {"error": str(e)}