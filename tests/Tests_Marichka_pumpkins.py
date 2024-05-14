from src.Marichka_pumpkins import gardener_bot
import unittest


class TestOfRobotsWays(unittest.TestCase):

    def test_5_5(self):
        arr_1 = [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]]

        expected_result = [21, 16, 11, 6, 1, 2, 7, 12, 17, 22, 23, 18, 13, 8, 3, 4, 9, 14, 19, 24, 25, 20, 15, 10, 5]
        self.assertEqual(gardener_bot(arr_1), expected_result)

    def test_4_2(self):
        arr_2 = [[1, 2, 3, 4],
                 [5, 6, 7, 8]]

        expected_result = [5, 1, 2, 6, 7, 3, 4, 8]
        self.assertEqual(gardener_bot(arr_2), expected_result)

    def test_1_6(self):
        arr_3 = [[1],
                 [7],
                 [11],
                 [16],
                 [1],
                 [12]]

        expected_result = [12, 1, 16, 11, 7, 1]
        self.assertEqual(gardener_bot(arr_3), expected_result)
