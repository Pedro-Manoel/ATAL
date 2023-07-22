def simple_bfs(graph, start, visited = None):
    if visited is None:
        visited = set()

    queue = []    
    visited.add(start)
    queue.append(start)
    
    while queue:
        vertex = queue.pop()
        print(vertex)
        
        for adj in graph[vertex]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)
    
    return visited

# Example
graph = {
    "s": ["w", "r"],
    "w": ["s", "t", "x"],
    "r": ["s", "v"],
    "v": ["r"],
    "t": ["w", "u", "x"],
    "x": ["w", "y", "t"],
    "u": ["t", "y"],
    "y": ["x", "u"]
}

simple_bfs(graph, "s")