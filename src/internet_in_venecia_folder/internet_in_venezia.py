def prim_mst(graph):
    n = len(graph)
    visited = [False] * n
    start_vertex = 0
    visited[start_vertex] = True
    mst_cost = 0

    while True:
        min_weight = float('inf')
        min_edge = None

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and 0 < graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        min_edge = (i, j)

        if min_edge is None:
            break

        u, v = min_edge
        visited[v] = True
        mst_cost += min_weight

    return mst_cost

def read_graph(data):
    graph = []
    with open(data, 'r') as file:
        for line in file:
            graph.append(list(map(int, line.strip().split(';'))))
    return graph

