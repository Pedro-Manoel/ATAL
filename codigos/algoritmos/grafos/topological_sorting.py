def dfs_order(graph, start, visited):
    order = []    
    visited.add(start)

    for adj in graph[start]:
        if adj not in visited:
            order += dfs_order(graph, adj, visited)
    
    return order + [start]

def topological_sorting(graph, start = None):
    visited = set()
    order = []

    if start:
        order += dfs_order(graph, start, visited)

    for vertex in graph.keys():
        if vertex not in visited:
            order += dfs_order(graph, vertex, visited)

    return order[::-1]

# Example
graph = {
    "r": ["v", "s"],
    "s": ["w"],
    "v": ["w", "s"],
    "w": [],
    "t": ["w", "x"],
    "x": []
}

result = topological_sorting(graph, "r")
print(*result)