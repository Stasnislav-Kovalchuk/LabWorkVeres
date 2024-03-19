import unittest
from hamstersShops import max_hamsters


class TestOfHamsters(unittest.TestCase):
    def test_1(self):
        s = 7
        hamsters = [[1, 2],
                    [2, 2],
                    [3, 1]]

        expected_result = 2
        self.assertEqual(max_hamsters(s, hamsters), expected_result)

    def test_2(self):
        s = 19
        hamsters = [[5, 0],
                    [2, 2],
                    [1, 4],
                    [5, 1]]

        expected_result = 3
        self.assertEqual(max_hamsters(s, hamsters), expected_result)

    def test_3(self):
        s = 2
        hamster = [[1, 50000],
                   [1, 60000]]

        expected_result = 1
        self.assertEqual(max_hamsters(s, hamster), expected_result)
