
import unittest
from features import reports


class TestAverageScore(unittest.TestCase):

    def test_average_score_normal(self):
        data = {"history": [80, 90, 100]}
        result = reports.average_score(data)
        self.assertEqual(result, 90.0)

    def test_average_score_empty(self):
        data = {"history": []}
        result = reports.average_score(data)
        self.assertEqual(result, 0.0)

    def test_average_score_rounding(self):
        data = {"history": [80, 85, 90]}
        result = reports.average_score(data)
        self.assertEqual(result, 85.0)


if __name__ == "__main__":
    unittest.main()
