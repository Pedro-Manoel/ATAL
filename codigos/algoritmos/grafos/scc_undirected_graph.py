def dfs_comp(graph, start, visited):
    component = [start]    
    visited.add(start)

    for adj in graph[start]:
        if adj not in visited:
            component += dfs_comp(graph, adj, visited)

    return component

def scc_undirected_graph(graph):
    components = []
    visited = set()
    
    for vertex in graph.keys():
        if vertex not in visited:
            components.append(dfs_comp(graph, vertex, visited))
    
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

components = scc_undirected_graph(graph)
print("\nComponents:")
for component in components:
    print(*component)