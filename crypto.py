import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API_URL = "https://api.coingecko.com/api/v3/simple/price"

COIN_ALIASES = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana",
    "doge": "dogecoin",
    "ada": "cardano",
    "xrp": "ripple",
}

DEFAULT_CURRENCY = "aud"


def resolve_coin_id(coin):
    coin = coin.strip().lower()
    return COIN_ALIASES.get(coin, coin)


def fetch_prices(coin_ids, currency=DEFAULT_CURRENCY):
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": currency,
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"

    request = urllib.request.Request(url, headers={"User-Agent": "crypto-tracker"})
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode())


def format_price(value, currency):
    return f"{value:,.2f} {currency.upper()}"


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python3 crypto.py <coin> [coin2 ...] [--currency aud]")
        print("Example: python3 crypto.py bitcoin ethereum")
        print(f"Known shortcuts: {', '.join(sorted(COIN_ALIASES))}")
        sys.exit(1)

    currency = DEFAULT_CURRENCY
    if "--currency" in args:
        idx = args.index("--currency")
        currency = args[idx + 1].lower()
        del args[idx:idx + 2]

    coin_ids = [resolve_coin_id(coin) for coin in args]

    try:
        data = fetch_prices(coin_ids, currency)
    except urllib.error.URLError as error:
        print(f"Network error: {error}")
        sys.exit(1)

    for original, coin_id in zip(args, coin_ids):
        prices = data.get(coin_id)
        if not prices or currency not in prices:
            print(f"{original}: not found")
            continue
        print(f"{original}: {format_price(prices[currency], currency)}")


if __name__ == "__main__":
    main()
