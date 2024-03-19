import unittest
from heap_based_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def test_insert_to_queue(self):
        pq = PriorityQueue()

        pq.insert_to_queue(5, 3)
        pq.insert_to_queue(7, 1)
        pq.insert_to_queue(8, 8)
        pq.insert_to_queue(4, 8)
        pq.insert_to_queue(3, 4)
        pq.insert_to_queue(2, 8)

        expected_queue = [(8, 8), (8, 4), (8, 2), (1, 7), (4, 3), (3, 5)]
        actual_queue = [(node.priority, node.value) for node in pq.queue]
        self.assertEqual(actual_queue, expected_queue)

    def test_delete_first_priority(self):
        pq = PriorityQueue()

        pq.insert_to_queue(5, 3)
        pq.insert_to_queue(7, 1)
        pq.insert_to_queue(8, 8)
        pq.insert_to_queue(4, 8)
        pq.insert_to_queue(3, 4)
        pq.insert_to_queue(2, 8)

        pq.delete_first_priority()

        expected_queue = [(8, 4), (4, 3), (8, 2), (1, 7), (3, 5)]
        actual_queue = [(node.priority, node.value) for node in pq.queue]
        self.assertEqual(actual_queue, expected_queue)

    def test_display_queue(self):
        pq = PriorityQueue()

        pq.insert_to_queue(5, 3)
        pq.insert_to_queue(7, 1)
        pq.insert_to_queue(8, 8)
        pq.insert_to_queue(4, 8)
        pq.insert_to_queue(3, 4)
        pq.insert_to_queue(2, 8)

        expected_output = [(8, 8), (8, 4), (8, 2), (1, 7), (4, 3), (3, 5)]
        actual_output = [(node.priority, node.value) for node in pq.queue]

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
