import heapq

def format_table(data, title):
    print(title)
    print("--------------------")
    for vertex, value in data.items():
        print(f"{vertex}: {value}")
    print("\n")

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    parent={node:None for node in graph}

    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        for next_node, weight in graph[current_node].items():
            distance_temp = current_distance + weight
            if distance_temp < distances[next_node]:
                distances[next_node] = distance_temp
                parent[next_node] = current_node
                heapq.heappush(queue, (distance_temp, next_node))

    return distances, parent

# Example
graph = {
    "A": {"B": 2, "C": 1},
    "B": {"D": 1},
    "C": {"E": 4, "D": 3},
    "D": {"F": 2},
    "E": {"F": 2},
    "F": {}
}

distances, parents  = dijkstra(graph, "A")

format_table(distances, "Distances")
format_table(parents, "Parents")