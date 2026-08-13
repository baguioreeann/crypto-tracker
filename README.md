# Crypto Price Tracker

A small command-line tool that fetches live cryptocurrency prices from the
[CoinGecko API](https://www.coingecko.com/en/api) (no API key required).

## Usage

```bash
python3 crypto.py bitcoin ethereum
python3 crypto.py btc eth sol --currency eur
```

Supports shortcuts for common coins: `btc`, `eth`, `sol`, `doge`, `ada`, `xrp`.
Any other CoinGecko coin ID (e.g. `chainlink`) also works.

## Example output

```
$ python3 crypto.py btc eth sol
btc: 63,402.00 USD
eth: 1,876.51 USD
sol: 75.58 USD
```
