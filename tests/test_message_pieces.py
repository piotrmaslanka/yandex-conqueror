import unittest

from conqueror.msg_generator import MessagePiece


class TestMessages(unittest.TestCase):
    def test_something(self):
        mp = MessagePiece('1-A', '[1|2] [3|4] [5|6]')
        a = str(mp)
        self.assertTrue(a[0] == '1' or a[0] == '2')
        self.assertTrue(a[2] == '3' or a[2] == '4')
        self.assertTrue(a[4] == '5' or a[4] == '6')
