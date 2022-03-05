import unittest

from conqueror.utils.point_obtain import random_point


class TestObtainOrders(unittest.TestCase):
    def test_random_point(self):
        x, y = random_point(5)
        self.assertGreaterEqual(x, -5)
        self.assertLessEqual(x, 5)
        self.assertGreaterEqual(y, -5)
        self.assertLessEqual(y, 5)
