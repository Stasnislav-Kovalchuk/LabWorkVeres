import unittest
from src.dfa_haystack_and_needle import search_num_of_in


class TestSearchNumOfIn(unittest.TestCase):
    def test_single_occurrence(self):
        haystack = "ababaababbaa"
        needle = "aaba"
        expected_result = [4]
        self.assertEqual(search_num_of_in(needle, haystack), expected_result)

    def test_multiple_occurrences(self):
        haystack = "ababaababbaa"
        needle = "ab"
        expected_result = [0, 2, 5, 7]
        self.assertEqual(search_num_of_in(needle, haystack), expected_result)

    def test_no_occurrence(self):
        haystack = "ababaababbaa"
        needle = "xyz"
        expected_result = []
        self.assertEqual(search_num_of_in(needle, haystack), expected_result)


if __name__ == '__main__':
    unittest.main()
