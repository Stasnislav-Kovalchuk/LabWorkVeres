import unittest
from src.GameServer import *


class MyTestCase(unittest.TestCase):
    def test_case_example_1(self):
        ping('input_for_GM.txt', 'output_for_GM.txt')
        file = open('output_for_GM.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 100)

    def test_case_example_2(self):
        ping('input_for_GM2.txt', 'output_for_GM2.txt')
        file = open('output_for_GM2.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10)

    def test_case_example_3(self):
        ping('input_for_GM3.txt', 'output_for_GM3.txt')
        file = open('output_for_GM3.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 1000000000)

    #
    def test_case_example_4(self):
        ping('input_for_GM4.txt', 'output_for_GM4.txt')
        file = open('output_for_GM4.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 0)


#
#
if __name__ == '__main__':
    unittest.main()
