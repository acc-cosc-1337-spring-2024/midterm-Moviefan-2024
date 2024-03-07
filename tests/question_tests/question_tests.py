# question_tests.py
import unittest
from question_a import get_person_category

class TestGetPersonCategory(unittest.TestCase):
    def test_categories(self):
        self.assertEqual(get_person_category(1), "infant")
        self.assertEqual(get_person_category(2), "child")
        self.assertEqual(get_person_category(14), "teenager")
        self.assertEqual(get_person_category(20), "adult")

if __name__ == "__main__":
    unittest.main()

    import unittest
from question_b import get_day_of_week

class TestDayOfWeek(unittest.TestCase):
    def test_values(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(8), "Invalid number")

if __name__ == "__main__":
    unittest.main()


    import unittest
from question_c import get_random_number

class TestGetRandomNumber(unittest.TestCase):
    def test_get_random_number(self):
        for _ in range(1000):
            number = get_random_number()
            self.assertTrue(1 <= number <= 5)

if __name__ == '__main__':
    unittest.main()


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
