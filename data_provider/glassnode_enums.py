from enum import Enum

VERSION = 'v1'
METRICS = '/metrics/'
BASE_URL = f'https://api.glassnode.com/{VERSION}{METRICS}'
ADDRESSES = 'addresses/'
FEES = 'fees/'
INSTITUTIONS = 'institutions/'
SUPPLY = 'supply/'
INDICATORS = 'indicators/'
BLOCKCHAIN = 'blockchain/'
MINING = 'mining/'
TRANSACTIONS = 'transactions/'
MARKET = 'market/'


# now can load up to T2 metrics
class AddressesGN(Enum):
    # Address Activity
    active_addresses = ADDRESSES + 'active_count'  # T1
    sending_addresses = ADDRESSES + 'sending_count'  # T1
    receiving_addresses = ADDRESSES + 'receiving_count'  # T1

    # Address Growth
    new_addresses = ADDRESSES + 'new_non_zero_count'  # T1
    total_addresses = ADDRESSES + 'count'  # T1


class FeesGN(Enum):
    fees_total = FEES + 'volume_sum'  # T1
    fees_mean = FEES + 'volume_mean'  # T1
    fees_median = FEES + 'volume_median'  # T1  


class InstitutionsGN(Enum):
    grayscale_holdings = INSTITUTIONS + 'grayscale_holdings_sum'  # T1
    grayscale_flows = INSTITUTIONS + 'grayscale_flows_sum'  # T1
    grayscale_premium = INSTITUTIONS + 'grayscale_premium_percent'  # T1
    grayscale_aum = INSTITUTIONS + 'grayscale_aum_sum'  # T1
    grayscale_market_price = INSTITUTIONS + 'grayscale_market_price_usd'  # T1
    purpose_etf_holdings = INSTITUTIONS + 'purpose_etf_holdings_sum'  # T1
    purpose_etf_flows = INSTITUTIONS + 'purpose_etf_flows_sum'  # T1
    qbtc_holdings = INSTITUTIONS + 'qbtc_holdings_sum'  # T1
    qbtc_flows = INSTITUTIONS + 'qbtc_flows_sum'  # T1
    qbtc_premium = INSTITUTIONS + 'qbtc_premium_percent'  # T1
    qbtc_aum = INSTITUTIONS + 'qbtc_aum_sum'  # T1
    qbtc_market_price = INSTITUTIONS + 'qbtc_market_price_usd'  # T1


class SupplyGN(Enum):
    supply_last_active_1y_ago = SUPPLY + 'active_more_1y_percent'  # T1
    circulating_supply = SUPPLY + 'current'  # T1


class IndicatorsGN(Enum):
    difficulty_ribbon = INDICATORS + 'difficulty_ribbon'  # T1
    SOPR = INDICATORS + 'sopr'  # T1
    stock_to_flow_ratio = INDICATORS + 'stock_to_flow_ratio'  # T1
    stock_to_flow_deflection = INDICATORS + 'stock_to_flow_deflection'  # T2


class BlockchainGN(Enum):
    block_height = BLOCKCHAIN + 'block_height'  # T1
    block_minded = BLOCKCHAIN + 'block_count'  # T1
    block_interval_mean = BLOCKCHAIN + 'block_interval_mean'  # T1
    block_interval_median = BLOCKCHAIN + 'block_interval_median'  # T1
    block_size_mean = BLOCKCHAIN + 'block_size_mean'  # T1
    block_size_total = BLOCKCHAIN + 'block_size_sum'  # T1
    utxos_created = BLOCKCHAIN + 'utxo_created_count'  # T1
    utxos_total = BLOCKCHAIN + 'utxo_count'  # T1
    utxos_spent = BLOCKCHAIN + 'utxo_spent_count'  # T1
    utxo_value_created_total = BLOCKCHAIN + 'utxo_created_value_sum'  # T1
    utxo_value_spent_total = BLOCKCHAIN + 'utxo_spent_value_sum'  # T1
    utxo_value_created_mean = BLOCKCHAIN + 'utxo_created_value_mean'  # T1
    utxo_value_spent_mean = BLOCKCHAIN + 'utxo_spent_value_mean'  # T1
    utxo_value_created_median = BLOCKCHAIN + 'utxo_created_value_median'  # T1
    utxo_value_spent_median = BLOCKCHAIN + 'utxo_spent_value_median'  # T1


class MiningGN(Enum):
    difficulty = MINING + 'difficulty_latest'  # T1
    hash_rate = MINING + 'hash_rate_mean'  # T1
    # accumulation_addresses = ADDRESSES+ 'accumulation_count' # T1
    # accumulation_balance = ADDRESSES + 'accumulation_balance'


class TransactionsGN(Enum):
    transaction_count = TRANSACTIONS + 'count'  # T1
    transaction_rate = TRANSACTIONS + 'rate'  # T1
    transaction_size_total = TRANSACTIONS + 'size_sum'  # T1
    transaction_size_mean = TRANSACTIONS + 'size_mean'  # T1
    transfers_volume_total = TRANSACTIONS + 'transfers_volume_sum'  # T1
    transfers_volume_mean = TRANSACTIONS + 'transfers_volume_mean'  # T1
    transfers_volume_median = TRANSACTIONS + 'transfers_volume_median'  # T1


class MarketGN(Enum):
    price = MARKET + 'price_usd_close'  # T1
    price_OHLC = MARKET + 'price_usd_ohlc'  # T1
    price_drawdown_from_ATH = MARKET + 'price_drawdown_relative'  # T1

    # class Entities(Enum):
    #     sending_count = 'sending_count'
    #     receiving_count = 'receiving_count'

    # class Addresses(Enum):
    #     sending_to_exchanges_count = VERSION + METRICS +
    # class EndPoint(Enum):
    #     Addresses = VERSION + '/metrics/addresses/'
    #     Blockchain = VERSION + '/metrics/blockchain/'
    #     Derivatives = VERSION + '/metrics/derivatives/'
    #     Distribution = VERSION + '/metrics/distribution/'
    #     Entities = Entities
