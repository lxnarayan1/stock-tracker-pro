import yfinance as yf

def get_stock_quote(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")

        if hist.empty:
            return None

        return {
            "symbol": symbol.upper(),
            "price": hist["Close"].iloc[-1],
            "currency": "USD",
            "volume": int(hist["Volume"].iloc[-1]),
            "last_trading_day": hist.index[-1].strftime("%Y-%m-%d"),
        }
    except Exception as e:
        print("Error in get_stock_quote:", e)
        return None


def get_company_overview(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "symbol": symbol.upper(),
            "name": info.get("longName", ""),
            "sector": info.get("sector", ""),
            "industry": info.get("industry", ""),
            "market_cap": info.get("marketCap", ""),
            "description": info.get("longBusinessSummary", ""),
        }
    except Exception as e:
        print("Error in get_company_overview:", e)
        return None


def search_symbols(query):
   
    suggestions = []
    query = query.lower()

    
    popular_stocks = {
        "AAPL": "Apple Inc.",
        "MSFT": "Microsoft Corporation",
        "GOOGL": "Alphabet Inc.",
        "AMZN": "Amazon.com, Inc.",
        "TSLA": "Tesla, Inc.",
        "IBM": "International Business Machines Corporation",
        "NFLX": "Netflix, Inc."
    }

    for symbol, name in popular_stocks.items():
        if query in symbol.lower() or query in name.lower():
            suggestions.append({"symbol": symbol, "name": name})

    return suggestions
