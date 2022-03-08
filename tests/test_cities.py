import unittest

from conqueror.app import app
from conqueror.scraper.data_reader import read_cities


class TestMessages(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_cities(self):
        p = read_cities()
        self.assertGreaterEqual(len(p), 1)

    def test_view_cities(self):
        resp = self.client.get('/v1/view-cities')
        self.assertGreaterEqual(len(resp.get_json()), 1)
