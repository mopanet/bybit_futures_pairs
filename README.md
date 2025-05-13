Yes, it would be a good idea to update the README to reflect the changes made to the script. Specifically, you should mention the additional filter for futures pairs with expiration dates. Here's an updated section for the README:

### Updated README:

````markdown
# Bybit Futures Pairs by Market Cap

This Python script fetches the list of Bybit linear futures pairs, filters for USDT pairs, excludes options and futures pairs with expiration dates, sorts them by market cap, and outputs the top pairs in a format suitable for importing to TradingView.

## Features

- Fetches Bybit futures pairs using the Bybit API
- Filters only the pairs that are USDT-based
- Excludes options and futures pairs with expiration dates (e.g., `-23MAY25`)
- Sorts the pairs by market cap (24h volume * last price)
- Limits the output to the top 50 pairs (can be configured)
- Outputs the symbols in a comma-separated list for easy import to TradingView

## Requirements

- Python 3.x
- `requests` library

You can install the required dependencies with the following:

```bash
pip install requests
````

## Usage

1. Clone or download the repository to your local machine.
2. Modify the `MAX_PAIRS` variable in the script to adjust the number of pairs you want to fetch (default is 50).
3. Run the script:

```bash
python bybit_futures_pairs.py
```

4. The output will be a comma-separated list of USDT futures pairs, sorted by market cap, excluding options and futures with expiration dates.

## Example Output

```
BTCUSDT,ETHUSDT,LTCUSDT,...
```

You can then import this list into TradingView for analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

The only real change is the exclusion of expiration date futures and options pairs, which is now part of the functionality.

Let me know if you'd like any further edits!
```
