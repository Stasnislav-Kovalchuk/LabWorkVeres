import unittest
from GameServer import *


class MyTestCase(unittest.TestCase):
    def test_case_example_1(self):
        ping('input.txt', 'output.txt')
        file = open('output.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 100)

    def test_case_example_2(self):
        ping('input2.txt', 'output2.txt')
        file = open('output2.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 10)

    def test_case_example_3(self):
        ping('input3.txt', 'output3.txt')
        file = open('output3.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 1000000000)

    #
    def test_case_example_4(self):
        ping('input4.txt', 'output4.txt')
        file = open('output4.txt', 'r')
        result = int(file.readline())
        file.close()
        self.assertEqual(result, 0)


#
#
if __name__ == '__main__':
    unittest.main()
