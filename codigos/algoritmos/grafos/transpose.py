def transpose(graph):
    transpose = {node: [] for node in graph}

    for node in graph:
        for adj in graph[node]:
            transpose[adj].append(node)

    return transpose

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

graphT = transpose(graph)

print("Trasnpose Graph:")
for node in graphT:
    print(f'{node}: {graphT[node]}')
