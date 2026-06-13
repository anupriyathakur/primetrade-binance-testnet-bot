# Binance Futures Testnet Trading Bot

## Overview

This project is a Python CLI application that places Market and Limit orders on Binance Futures Testnet (USDT-M).

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Input validation
* Logging
* Error handling
* Binance Futures Testnet integration

## Requirements

* Python 3.10+
* Binance Futures Testnet Account
* API Key and Secret Key

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

## Run Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

## Project Structure

```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
├── cli.py
├── requirements.txt
├── README.md
├── .env.example
```

## Assumptions

* Binance Futures Testnet API credentials are valid.
* User has sufficient testnet balance.
* Internet connection is available.
