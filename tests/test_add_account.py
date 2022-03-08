import unittest

from conqueror.run import app
from conqueror.cassandra import session


class TestAddAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_add_account(self):
        resp = self.client.put('/v1/add-yandex-account', json={'email': 'test@example.com',
                                                               'password': '1234'})
        self.assertEqual(resp.status_code, 201)
        d = list(session.execute('SELECT * FROM accounts WHERE email=%s', ('test@example.com', )))
        self.assertEqual(len(d), 1)

    def test_add_review(self):
        resp = self.client.get('/v1/add-review/test@example.com')
        self.assertEqual(resp.status_code, 204)
        resp = self.client.get('/v1/view-reviews')
        self.assertEqual(resp.status_code, 200)
        print(resp.data)
        self.assertGreaterEqual(resp.get_json()['entries'], 1)
