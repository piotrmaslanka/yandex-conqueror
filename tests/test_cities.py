import unittest

from conqueror.msg_generator import MessagePiece, get_messages
from conqueror.scraper.data_reader import read_cities


class TestMessages(unittest.TestCase):
    def test_cities(self):
        p = read_cities()
        self.assertGreaterEqual(len(p), 1)
