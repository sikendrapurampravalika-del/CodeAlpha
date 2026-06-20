import json
import urllib.error
import urllib.request

SAMPLE_DATA = {
    "AAPL": {
        "longName": "Apple Inc.",
        "symbol": "AAPL",
        "regularMarketPrice": 175.23,
        "regularMarketChange": -1.34,
        "regularMarketChangePercent": -0.76,
        "currency": "USD",
        "regularMarketVolume": 55432000,
        "marketCap": 2745000000000,
    },
    "MSFT": {
        "longName": "Microsoft Corporation",
        "symbol": "MSFT",
        "regularMarketPrice": 331.16,
        "regularMarketChange": 0.81,
        "regularMarketChangePercent": 0.25,
        "currency": "USD",
        "regularMarketVolume": 24480000,
        "marketCap": 2500000000000,
    },
    "GOOGL": {
        "longName": "Alphabet Inc.",
        "symbol": "GOOGL",
        "regularMarketPrice": 142.83,
        "regularMarketChange": -0.42,
        "regularMarketChangePercent": -0.29,
        "currency": "USD",
        "regularMarketVolume": 1934000,
        "marketCap": 1820000000000,
    },
}


def fetch_stock_data(symbol: str) -> dict:
    symbol = symbol.strip().upper()
    if not symbol:
        return {}

    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            body = response.read().decode("utf-8")
            data = json.loads(body)
            result = data.get("quoteResponse", {}).get("result", [])
            if not result:
                return {}
            return result[0]
    except (urllib.error.URLError, json.JSONDecodeError, ValueError):
        return {}


def format_number(value):
    if value is None:
        return "N/A"
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float):
        return f"{value:.2f}"
    return str(value)


def print_stock_summary(info: dict):
    if not info:
        print("No data available for that ticker. Try AAPL, MSFT, or GOOGL.")
        return

    name = info.get("longName") or info.get("shortName") or info.get("symbol")
    symbol = info.get("symbol", "N/A")
    price = format_number(info.get("regularMarketPrice"))
    change = format_number(info.get("regularMarketChange"))
    percent = format_number(info.get("regularMarketChangePercent"))
    currency = info.get("currency", "")
    volume = format_number(info.get("regularMarketVolume"))
    market_cap = format_number(info.get("marketCap"))

    print(f"\n{symbol} - {name}")
    print(f"Price: {price} {currency}")
    print(f"Change: {change} ({percent}%)")
    print(f"Volume: {volume}")
    print(f"Market Cap: {market_cap}")


def main():
    print("Stock Price Tracker")
    print("Enter a stock ticker symbol like AAPL, MSFT, or GOOGL.")

    symbol = input("Ticker: ").strip()
    if not symbol:
        print("Ticker symbol is required.")
        return

    stock_info = fetch_stock_data(symbol)
    if not stock_info:
        stock_info = SAMPLE_DATA.get(symbol.upper(), {})
        if stock_info:
            print("\nUnable to fetch live data. Showing fallback sample data.")

    print_stock_summary(stock_info)


if __name__ == "__main__":
    main()
