import unittest
import json
from app import app

class PointsTrackerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_given_tests(self):
        transactions = [
            { "payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z" },
            { "payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z" },
            { "payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z" },
            { "payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z" },
            { "payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z" }
        ]
        for tx in transactions:
            response = self.app.post('/add', json=tx)
            self.assertEqual(response.status_code, 200)

        response = self.app.post('/spend', json={"points": 5000})
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/balance')
        self.assertEqual(response.status_code, 200)
        expected = {
            "DANNON": 1000,
            "UNILEVER" : 0,
            "MILLER COORS": 5300
        }
        self.assertEqual(json.loads(response.data), expected)

if __name__ == '__main__':
    unittest.main()
