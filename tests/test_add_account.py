import unittest

from conqueror.run import app


class TestAddAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_apispec(self):
        resp = self.client.get('/apispec_1.json')
        self.assertEqual(resp.status_code, 200)

    def test_add_review(self):
        resp = self.client.get('/v1/add-review/test@example.com')
        self.assertEqual(resp.status_code, 204)
        resp = self.client.get('/v1/view-reviews')
        self.assertEqual(resp.status_code, 200)
        print(resp.data)
        self.assertGreaterEqual(resp.get_json()['entries'], 1)
