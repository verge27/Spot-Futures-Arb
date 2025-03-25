import time
import logging
from db import log_trade
from utils import get_funding_rate, get_order_book_prices

SPREAD_THRESHOLD = 0.5  # in percentage
TRADE_AMOUNT = 0.01


def calculate_spread(spot_price, futures_price):
    return ((futures_price - spot_price) / spot_price) * 100


def execute_trade(symbol, spot_exchange, futures_exchange, spot_price, futures_price):
    spread = calculate_spread(spot_price, futures_price)
    funding_rate = get_funding_rate(futures_exchange, symbol)

    if spread >= SPREAD_THRESHOLD and (funding_rate is None or funding_rate < 0.1):
        logging.info(f"[PAPER TRADE] Arbitrage: Buy {symbol} on {spot_exchange} at {spot_price}, "
                     f"Short on {futures_exchange} at {futures_price}, Spread: {spread:.2f}%")

        log_trade(symbol, spot_exchange, futures_exchange, spot_price, futures_price, spread)
        return True

    return False


def run_arbitrage(symbols, exchanges):
    while True:
        for symbol in symbols:
            for spot_name, spot_ex in exchanges.items():
                spot_price = get_order_book_prices(spot_ex['spot'], symbol)
                if not spot_price:
                    continue

                for fut_name, fut_ex in exchanges.items():
                    if spot_name == fut_name:
                        continue

                    futures_price = get_order_book_prices(fut_ex['futures'], symbol)
                    if not futures_price:
                        continue

                    execute_trade(symbol, spot_name, fut_name, spot_price, futures_price)
        time.sleep(10)
