def bellman_ford(graph, node):
    distances = {node:float('inf') for node in graph}
    nodes = graph.keys()
    distances[node] = 0

    for _ in range(len(nodes) - 1):
        for current_node in nodes:
            for next_node, weight in graph[current_node].items():
                distance_temp = distances[current_node] + weight
                if distance_temp < distances[next_node]:
                    distances[next_node] = distance_temp

    for current_node in nodes:
        for next_node, weight in graph[current_node].items():
            distance_temp = distances[current_node] + weight
            if distance_temp < distances[next_node]:
                return (False, distances)
            
    return (True, distances)

# Example
graph = {
    "z": {"u": 6, "x": 7},
    "u": {"v": 5, "x": 8, "y": -4},
    "v": {"u": -2},
    "x": {"v": -3, "y": 9},
    "y": {"z": 2, "v": 7},
}

negative_cycles, vertices = bellman_ford(graph, "z")

print(f'Graph contains negative cycles: {not negative_cycles}')
if negative_cycles:
    for vertice in vertices:
        print(f'{vertice}: {vertices[vertice]}')
