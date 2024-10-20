import yfinance as yf

def fetch_historical_stock_data(ticker, interval, period):
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

def fetch_historical_currency_data(currency_pair, interval, period):
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

def fetch_current_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.history(interval='1d', period='1d')

        data = []
        for index, row in stock_info.iterrows():
            if index.strftime('%Y-%m-%d'):
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

def fetch_current_currency_data(currency_pair):
    try:
        currency = yf.Ticker(currency_pair)
        stock_info = currency.history(interval='1d', period='1d')

        data = []
        for index, row in stock_info.iterrows():
            if index.strftime('%Y-%m-%d'):
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


def convert_asset_to_currency(ticker, value, asset_type, convert_to='EUR'):
    try:
        currency_pair = f"{convert_to} {ticker}"
        exchange_rate_data = yf.download(currency_pair, period='1d')

        if exchange_rate_data.empty:
            return {"error": f"Exchange rate data for {currency_pair} not found."}

        exchange_rate = exchange_rate_data['Close'].iloc[-1]
        print(exchange_rate)
        # converted_value = value * exchange_rate

        return ticker, asset_type, exchange_rate_data['Close']

    except IndexError:
        return {"error": f"No data found for {currency_pair}, symbol may be delisted."}
    except Exception as e:
        return {"error": str(e)}