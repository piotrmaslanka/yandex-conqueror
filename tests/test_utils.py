import unittest

from conqueror.utils import degrees_to_kilometers_lat, kilometers_to_degrees_lat


class MyCastKilometres(unittest.TestCase):
    def test_lat(self):
        a = degrees_to_kilometers_lat(50)
        self.assertEqual(50, kilometers_to_degrees_lat(a))
