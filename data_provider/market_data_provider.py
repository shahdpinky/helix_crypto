import time
from datetime import datetime
from pathlib import Path

import pandas as pd

OHLVCV_COL = ['unix_time', 'open', 'high', 'low', 'close', 'volume']
DATA_FOLDER = data_folder = Path('/Users/cedricwang/ft_userdata/user_data/data/')


# get all data of these pairs
def file_name(pair, freq):
    name = f"{pair.replace('/', '_')}-{freq}.json"
    return name


def convert_unix_to_datetime(x):
    return datetime.utcfromtimestamp(int(x / 1000))


def read_ochlv_json(pair, exchange, timeframe):
    file_to_open = DATA_FOLDER / exchange / file_name(pair, timeframe)
    raw_data_df = pd.read_json(file_to_open)
    raw_data_df.columns = OHLVCV_COL
    raw_data_df['date'] = raw_data_df['unix_time'].apply(lambda x: convert_unix_to_datetime(int(x)))
    return raw_data_df


def get_freqtrade_ohlcv(symbol_list, exchange, timeframe):
    signle_pair_df_list = []
    for pair in set(symbol_list):
        try:
            signle_pair_df = read_ochlv_json(pair, exchange, timeframe)
            signle_pair_df['pair'] = pair
            signle_pair_df_list.append(signle_pair_df)
        except Exception as e:
            print(e)
    res_df = pd.concat(signle_pair_df_list)
    res_df = res_df.set_index(['pair', 'date'])
    return res_df


def get_ccxt_ohlcv(symbol_list, exchange, timeframe):
    all_res_df = pd.DataFrame()
    for symbol in symbol_list:
        time.sleep(exchange.rateLimit / 1000)  # time.sleep wants seconds
        print(symbol)
        symbol_res = exchange.fetch_ohlcv(symbol, timeframe=timeframe)  # ftx 1500 limit
        symbol_res_df = pd.DataFrame(symbol_res, columns=OHLVCV_COL)
        symbol_res_df['symbol'] = symbol
        all_res_df = pd.concat([all_res_df, symbol_res_df])

    all_res_df['time_tick'] = all_res_df['unix_time'].apply(lambda x: datetime.utcfromtimestamp(int(x / 1000)))
    all_res_df = all_res_df.set_index(['symbol', 'time_tick'])

    return all_res_df
