# Crypto Price Tracker

A small command-line tool that fetches live cryptocurrency prices from the
[CoinGecko API](https://www.coingecko.com/en/api) (no API key required).

## Usage

```bash
python3 crypto.py bitcoin ethereum
python3 crypto.py btc eth sol --currency usd
```

Prices default to AUD. Supports shortcuts for common coins: `btc`, `eth`, `sol`,
`doge`, `ada`, `xrp`. Any other CoinGecko coin ID (e.g. `chainlink`) also works.

## Example output

```
$ python3 crypto.py btc eth sol
btc: 89,840.00 AUD
eth: 2,659.14 AUD
sol: 107.05 AUD
```
