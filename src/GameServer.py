from heap_priority_queue import *


def dijkstra(server, vertex_n, clients, adjacency_list):
    temp_max_ping = 0
    heap = PriorityQueue()
    heap.insert(server, 0)
    dist_to = {}
    for vertex in range(vertex_n + 1):
        dist_to[vertex] = float('inf')
    dist_to[server] = 0
    visited = set()

    while heap.array:
        vertex = heap.delete_first_priority()
        if vertex is None:
            break

        if vertex in clients:
            temp_max_ping = max(temp_max_ping, dist_to[vertex])

        if vertex in visited:
            continue

        visited.add(vertex)
        for neighbour, weight in adjacency_list[vertex - 1]:
            if dist_to.get(neighbour, float('inf')) > dist_to[vertex] + weight:
                dist_to[neighbour] = dist_to[vertex] + weight
                heap.insert(neighbour, dist_to[neighbour])

    return temp_max_ping


def ping(input_file, output_file):
    file = open(input_file, 'r')
    first_line = file.readline()
    if not first_line:
        write_output(output_file, None)
        file.close()
        return

    vertex_n, edge_n = map(int, first_line.split(' '))
    gamers = list(map(int, file.readline().split(' ')))
    router_list = [router for router in range(1, vertex_n + 1) if router not in gamers]
    adjacency_list = [[] for _ in range(vertex_n)]
    for _ in range(edge_n):
        vertex, neighbour, weight = map(int, file.readline().split(' '))
        adjacency_list[vertex - 1].append([neighbour, weight])
        adjacency_list[neighbour - 1].append([vertex, weight])

    file.close()

    min_max_ping = float('inf')
    for server in router_list:
        min_max_ping = min(min_max_ping, dijkstra(server, vertex_n, gamers, adjacency_list))

    write_output(output_file, min_max_ping)


def write_output(output_file_path, result):
    file = open(output_file_path, 'w')
    file.write(str(result))
    file.close()
    return
