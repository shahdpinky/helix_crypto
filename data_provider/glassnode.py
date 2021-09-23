from datetime import date, datetime

import pandas as pd
import requests

from data_provider.data_provider import DataProvider
from data_provider.glassnode_enums import BASE_URL
from enums import Asset

API_KEY = '1wuhLy55NVrwdPTpPUTkHpxwkWI'


class GlassNodeKey:
    def __init__(self, end_point, asset: Asset, frequency=None, currency=None):
        """
        Key for GlassNodeProvider
        :param end_point:
        :param asset:
        :param frequency:
        :param currency:
        """
        self.end_point = end_point
        self.asset = asset
        self.frequency = frequency
        self.currency = currency

    def value(self):
        """
        API params from the key
        :return: dict
        """
        end_point_val = self.end_point.value
        param_dict = {
            'a': self.asset.value,
            'i': self.frequency,
            'c': self.currency,
        }
        return end_point_val, param_dict


class GlassNodeProvider(DataProvider):
    def __init__(self):
        """
        GlassNode API Wrapper
        """
        self._api_key = API_KEY
        super(GlassNodeProvider, self).__init__()

    @property
    def api_key(self):
        return self._api_key

    def set_api_key(self, value):
        self._api_key = value

    def get(self, key, start_time=None, end_time=None):
        if not isinstance(key, GlassNodeKey):
            raise ValueError(f'{type(key)} type is not supported.')
        end_point_val, param_dict = key.value()
        param_dict['api_key'] = self.api_key
        if start_time:
            if isinstance(start_time, date):
                param_dict['s'] = int(datetime.combine(start_time, datetime.min.time()).timestamp())
            else:
                param_dict['s'] = int(start_time.timestamp())

        if end_time:
            if isinstance(end_time, date):
                param_dict['u'] = int(datetime.combine(end_time, datetime.min.time()).timestamp())
            else:
                param_dict['u'] = int(end_time.timestamp())

        url = BASE_URL + end_point_val
        response = requests.get(
            url=url,
            params=param_dict,
        )

        try:
            response.raise_for_status()
        except Exception as e:
            # print(e)
            # print(response.text)
            raise e

        try:
            response_df = pd.read_json(response.text, convert_dates=['t'])
            response_df = response_df.set_index('t')
            response_df.index = pd.to_datetime(response_df.index, unit='s')
            response_df = response_df.sort_index()
            response_df.columns = ['_'.join(url.split('/')[-2:])]
            return response_df
        except Exception as e:
            # print(e)
            raise e

    def get_key(self):
        return GlassNodeKey
