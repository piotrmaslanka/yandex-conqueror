import unittest

from conqueror.utils.geom2d import degrees_to_kilometres, kilometres_to_degrees


class MyCastKilometres(unittest.TestCase):
    def test_lat(self):
        a = degrees_to_kilometres(50)
        self.assertEqual(50, kilometres_to_degrees(a))
