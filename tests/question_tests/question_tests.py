# question_tests.py
import unittest
from question_d import get_fahrenheit

class TestGetFahrenheit(unittest.TestCase):
    def test_0_celsius(self):
        self.assertEqual(get_fahrenheit(0), 32)

    def test_5_celsius(self):
        self.assertEqual(get_fahrenheit(5), 41)

    def test_10_celsius(self):
        self.assertEqual(get_fahrenheit(10), 50)

if __name__ == '__main__':
    unittest.main()
