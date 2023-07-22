def dfs_comp(graph, start, visited):
    component = [start]    
    visited.add(start)

    for adj in graph[start]:
        if adj not in visited:
            component += dfs_comp(graph, adj, visited)

    return component

def dfs_sort(graph, start, visited):
    order = []    
    visited.add(start)

    for adj in graph[start]:
        if adj not in visited:
            order += dfs_sort(graph, adj, visited)
    
    return order + [start]

def topological_sorting(graph, start = None):
    visited = set()
    order = []

    if start:
        order += dfs_sort(graph, start, visited)

    for vertex in graph.keys():
        if vertex not in visited:
            order += dfs_sort(graph, vertex, visited)

    return order[::-1]

def transpose(graph):
    transpose = {node: [] for node in graph}

    for node in graph:
        for adj in graph[node]:
            transpose[adj].append(node)

    return transpose

def scc_directed_graph(graph):
    topological_order = topological_sorting(graph)
    graphT = transpose(graph)
    components = []
    visited = set()
    
    for vertex in topological_order:
        if vertex not in visited:
            components.append(dfs_comp(graphT, vertex, visited))
    
    return components

# Example
graph = {
    "s": ["w", "v", "t"],
    "w": ["x"],
    "r": ["s"],
    "v": ["r", "w"],
    "t": ["u", "x"],
    "x": ["w", "y"],
    "u": ["t", "y"],
    "y": ["y"]
}

components = scc_directed_graph(graph)
print("\nComponents:")
for component in components:
    print(*component)




