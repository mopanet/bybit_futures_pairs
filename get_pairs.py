import requests
import json
import re

BYBIT_API_URL = 'https://api.bybit.com/v5/market/tickers?category=linear'
MAX_PAIRS = 100  # Parameter to limit the number of pairs


def fetch_bybit_futures_pairs(max_pairs):
    try:
        response = requests.get(BYBIT_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        pairs = []

        for item in data['result']['list']:
            # Ensure item is a dictionary
            if isinstance(item, dict):
                symbol = item.get('symbol')
      
                # Filtering condition update:
                if 'USDT' not in symbol or re.search(r'-\d{2}[A-Za-z]{3}\d{2}', symbol):
                  continue

                try:
                    volume_24h = float(item.get('turnover24h', 0))  # Updated key to 'turnover24h'
                    last_price = float(item.get('lastPrice', 0))    # Updated key to 'lastPrice'
                    market_cap = volume_24h * last_price
                    pairs.append((symbol, market_cap))
                except (ValueError, TypeError):
                    continue

        # Sort by market cap in descending order and limit to the specified number of pairs
        pairs.sort(key=lambda x: x[1], reverse=True)
        return pairs[:max_pairs]
    except requests.RequestException as e:
        print(f"Error fetching data from Bybit API: {e}")
        return []


def format_for_tradingview(pairs):
    # Extract just the symbols for TradingView
    return [pair[0] for pair in pairs]


def main():
    pairs = fetch_bybit_futures_pairs(MAX_PAIRS)
    if pairs:
        tradingview_list = format_for_tradingview(pairs)
        output = ','.join(tradingview_list)
        print(output)
    else:
        print("No data available to output.")


if __name__ == "__main__":
    main()
