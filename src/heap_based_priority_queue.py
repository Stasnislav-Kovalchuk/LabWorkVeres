class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i].priority < arr[left].priority:
            largest = left

        if right < n and arr[largest].priority < arr[right].priority:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def insert_to_queue(self, value, priority):
        node = Node(value, priority)
        self.queue.append(node)
        n = len(self.queue)
        for i in range(n // 2, - 1, -1):
            self.heapify(self.queue, n, i)

    def delete_first_priority(self):
        removed_element = self.queue[0]
        self.queue[0], self.queue[len(self.queue) - 1] = self.queue[len(self.queue) - 1], self.queue[0]
        print(f"Removed element{removed_element.priority}, {removed_element.value}")
        self.queue.pop()
        self.heapify(self.queue, len(self.queue), 0)

    def display_queue(self):
        print("Priority Queue:")
        for node in self.queue:
            print(node.priority, node.value)


# priority_queue = PriorityQueue()
# priority_queue.insert_to_queue(1, 3)
# priority_queue.insert_to_queue(2, 4)
# priority_queue.insert_to_queue(3, 6)
# priority_queue.insert_to_queue(1, 5)
# priority_queue.insert_to_queue(2, 2)
# priority_queue.insert_to_queue(3, 1)
# priority_queue.insert_to_queue(1, 7)
# priority_queue.insert_to_queue(2, 9)
# priority_queue.insert_to_queue(3, 8)
#
# priority_queue.display_queue()
#
# priority_queue.delete_first_priority()
#
# priority_queue.display_queue()
