import unittest

from conqueror.run import app
from conqueror.cassandra import session


class TestAddBusiness(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_add_business(self):
        resp = self.client.put('/v1/add-businesses', json=[{'businessId': '1234', 'sector': '1234'}])
        self.assertEqual(resp.status_code, 201)
        d = list(session.execute('SELECT * FROM businesses WHERE sector=%s', ('1234', )))
        self.assertEqual(len(d), 1)

        resp = self.client.get('/v1/view-businesses/1234')
        self.assertEqual(resp.status_code, 200)
        self.assertGreaterEqual(len(resp.data), 1)
