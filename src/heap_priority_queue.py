class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.array = []

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

        return self.array

    def insert(self, value, priority):
        node = Node(value, priority)
        self.array.append(node)
        n = len(self.array)
        for i in range(n // 2, -1, -1):
            self.heapify(self.array, n, i)

    def delete_first_priority(self):
        biggest = self.array[0]
        self.array[0], self.array[len(self.array) - 1] = self.array[len(self.array) - 1], self.array[0]
        self.array.pop()
        self.heapify(self.array, len(self.array), 0)
        return biggest.value

    def current_q(self):
        return [node.value for node in self.array]
