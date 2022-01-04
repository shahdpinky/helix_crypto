import ccxt
import pandas as pd
from datetime import datetime


def get_order_book_from_exchange(exchange, symbol, limit=5000):
    """
    Get order book as of now from exchange object
    :param exchange: e.g. cctx.binance
    :param symbol: e.g. BTC/USDT
    :param limit: depth limit
    :return: dataframe
    """
    current_time = datetime.now()
    order_book = exchange.fetch_order_book(symbol, limit=limit)
    order_book_clean = pd.DataFrame(order_book['bids'], columns=['bid_price', 'bid_amount'])
    append = pd.DataFrame(order_book['asks'], columns=['ask_price', 'ask_amount'])
    order_book_clean = pd.concat([order_book_clean, append], axis=1)
    order_book_clean['datetime'] = current_time
    order_book_clean['exchange'] = exchange.name
    order_book_clean['symbol'] = symbol

    return order_book_clean
