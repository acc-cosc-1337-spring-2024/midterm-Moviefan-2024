# question_tests.py
import unittest
from question_a import get_person_category

class TestGetPersonCategory(unittest.TestCase):

    def test_infant(self):
        self.assertEqual(get_person_category(1), "infant")

    def test_child(self):
        self.assertEqual(get_person_category(2), "child")

    def test_teenager(self):
        self.assertEqual(get_person_category(14), "teenager")

    def test_adult(self):
        self.assertEqual(get_person_category(20), "adult")

if __name__ == "__main__":
    unittest.main()
