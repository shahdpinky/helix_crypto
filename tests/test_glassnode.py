from datetime import date, datetime
from unittest import TestCase

from enums import Asset
from data_provider.glassnode_enums import AddressesGN
from data_provider.glassnode import GlassNodeProvider, GlassNodeKey


class TestGlassNodeProvider(TestCase):
    def setUp(self):
        self.key = GlassNodeKey(AddressesGN.new_addresses, Asset.BTC, frequency='24h', currency='USD')
        self.pvd = GlassNodeProvider()
        self.start_date = date(2021, 1, 1)
        self.end_date = date(2021, 5, 30)
        self.start_time = datetime(2021, 1, 1)
        self.end_time = datetime(2021, 5, 30)

    def test_get(self):
        time_res = self.pvd.get(self.key, self.start_time, self.end_time)
        date_res = self.pvd.get(self.key, self.start_date, self.end_date)
        self.assertAlmostEqual(time_res.sum().sum(), date_res.sum().sum())

    def test_get_key(self):
        self.assertTrue(self.pvd.get_key(), True)
