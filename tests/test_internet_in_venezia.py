import unittest
from src.internet_in_venezia import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        result = read_graph('Venezia_1.csv')
        self.assertEqual(result, [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ])

    def test_2(self):
        result = read_graph('Venezia_2.csv')
        self.assertEqual(result, [
            [0, 1, 0, 0],
            [1, 0, 2, 0],
            [0, 2, 0, 3],
            [0, 0, 3, 0]
        ])

    def test_3(self):
        result = read_graph('Venezia_3.csv')
        self.assertEqual(result, [
            [0, 5, 5, 5, 5],
            [5, 0, 5, 5, 5],
            [5, 5, 0, 5, 5],
            [5, 5, 5, 0, 5],
            [5, 5, 5, 5, 0]
        ])

    def test_4(self):
        graph = read_graph('Venezia_1.csv')
        result = prim_mst(graph)
        self.assertEqual(result, 2)

    def test_5(self):
        graph = read_graph('Venezia_2.csv')
        result = prim_mst(graph)
        self.assertEqual(result, 6)

    def test_6(self):
        graph = read_graph('Venezia_3.csv')
        result = prim_mst(graph)
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()

