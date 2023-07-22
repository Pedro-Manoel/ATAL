def simple_dfs(graph, start, visited = None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for adj in graph[start]:
        if adj not in visited:
            simple_dfs(graph, adj, visited)

    return visited

# Example
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

simple_dfs(graph, "A")