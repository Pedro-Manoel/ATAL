def format_table(data, title):
    print(title)
    print("--------------------")
    for vertex, value in data.items():
        print(f"{vertex}: {value}")
    print("\n")

def bfs(graph, start = None):
    colors = {}
    distance = {}
    parent = {}
    queue = []

    if start is None:
        start = list(graph.keys())[0]

    for vertex in graph:
        colors[vertex] = "WHITE"
        distance[vertex] = float('inf')
        parent[vertex] = None

    colors[start] = "GRAY"
    distance[start] = 0
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        for adj in graph[vertex]:
            if colors[adj] == "WHITE":
                colors[adj] = "GRAY"
                distance[adj] = distance[vertex] + 1
                parent[adj] = vertex
                queue.append(adj)
        colors[vertex] = "BLACK"

    return (colors, distance, parent)

# Example
graph = {
    "r": ["s", "v"],
    "s": ["r", "w"],
    "v": ["r"],
    "w": ["s", "t", "x"],
    "t": ["w", "x", "u"],
    "x": ["w", "t", "y"],
    "u": ["t", "y"],
    "y": ["x", "u"]
}

colors, distances, parents = bfs(graph, "r")

format_table(colors, "Colors")
format_table(distances, "Distances")
format_table(parents, "Parents")