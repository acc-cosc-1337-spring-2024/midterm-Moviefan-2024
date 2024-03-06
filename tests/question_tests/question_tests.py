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
