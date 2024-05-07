from heap_priority_queue import PriorityQueue


def prim_mst(graph: [[int]]) -> int:
    """
    its function to find sum of min span tree
    :param graph:
    :return: mst_cost (min span tree cost)
    """
    graph_length = len(graph)
    visited = set()
    start_vertex = 0
    visited.add(start_vertex)
    mst_cost = 0

    # Priority queue to store edges
    pq = PriorityQueue()

    # Add all edges from the start vertex to the priority queue
    for neighbor in range(graph_length):
        weight = graph[start_vertex][neighbor]
        if weight != 0:
            pq.insert((start_vertex, neighbor), weight)

    while pq.array:
        min_edge = pq.delete_first_priority()
        start_vertex, destination_vertex = min_edge

        if destination_vertex not in visited:
            visited.add(destination_vertex)
            mst_cost += graph[start_vertex][destination_vertex]

            for neighbor, weight in enumerate(graph[destination_vertex]):
                if weight != 0 and neighbor not in visited:
                    pq.insert((destination_vertex, neighbor), weight)

    return mst_cost


def read_graph(data: str) -> [[int]]:
    """

    :param data:
    :return: graph
    """
    graph = []
    with open(data, 'r') as file:
        for line in file:
            graph.append(list(map(int, line.strip().split(';'))))
    return graph
