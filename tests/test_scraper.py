import unittest

from conqueror.scraper.orders_obtainer import OrdersObtainer
from conqueror.utils.point_obtain import random_point


class TestObtainOrders(unittest.TestCase):
    def test_random_point(self):
        x, y = random_point(5)
        self.assertGreaterEqual(x, -5)
        self.assertLessEqual(x, 5)
        self.assertGreaterEqual(y, -5)
        self.assertLessEqual(y, 5)

    def test_orders_obtainer(self):
        oo = OrdersObtainer()
        oo.get_random_city()
        city = oo.get_random_city()
        pt_x, pt_y = oo.get_random_point(city)
