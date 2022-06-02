import unittest
from chart import Chart

class TestChart(unittest.TestCase):

    def test_secondsToText(self):
        self.assertEqual(Chart.secondsToText(1), '1 s')
        self.assertEqual(Chart.secondsToText(9), "9 s")
        self.assertEqual(Chart.secondsToText(10), "10 s")
        self.assertEqual(Chart.secondsToText(28), "28 s")
        self.assertEqual(Chart.secondsToText(59), "59 s")
        self.assertEqual(Chart.secondsToText(60), "1 min")
        self.assertEqual(Chart.secondsToText(3599), "59 min, 59 s")
        self.assertEqual(Chart.secondsToText(3600), "1 h")
        self.assertEqual(Chart.secondsToText(3601), "1 h, 1 s")
        self.assertEqual(Chart.secondsToText(3661), "1 h, 1 min, 1 s")
        self.assertEqual(Chart.secondsToText(86399), "23 h, 59 min, 59 s")
        self.assertEqual(Chart.secondsToText(86400), "24 h")
        self.assertEqual(Chart.secondsToText(86401), "24 h, 1 s")
        self.assertEqual(Chart.secondsToText(86461), "24 h, 1 min, 1 s")
        self.assertEqual(Chart.secondsToText(172800), "48 h")

if __name__ == '__main__':
    unittest.main()