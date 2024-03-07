import unittest
from question_c import get_random_number

class TestGetRandomNumber(unittest.TestCase):
    def test_get_random_number(self):
        for _ in range(1000):
            number = get_random_number()
            self.assertTrue(1 <= number <= 5)

if __name__ == '__main__':
    unittest.main()
