def format_table(data, title):
    print(title)
    print("--------------------")
    for vertex, value in data.items():
        print(f"{vertex}: {value}")
    print("\n")

def dfs_visit(vertex, graph, colors, parents, discovery_time, finish_time):
        colors[vertex] = 'GRAY'
        discovery_time[0] += 1
        finish_time[vertex] = None

        for adj in graph[vertex]:
            if colors[adj] == 'WHITE':
                parents[adj] = vertex
                dfs_visit(adj, graph, colors, parents, discovery_time, finish_time)

        colors[vertex] = 'BLACK'
        discovery_time[0] += 1
        finish_time[vertex] = discovery_time[0]

def dfs(graph, start = None):
    vertices = list(graph.keys())
    colors = {}
    parent = {}
    discovery_time = [0]
    finish_time = {}

    for vertex in vertices:
        colors[vertex] = 'WHITE'
        parent[vertex] = None

    if start:
         dfs_visit(start, graph, colors, parent, discovery_time, finish_time)

    for vertex in vertices:
        if colors[vertex] == 'WHITE':
            dfs_visit(vertex, graph, colors, parent, discovery_time, finish_time)

    return (colors, parent, finish_time)

# Example
graph = {
    "r": ["s", "v"],
    "s": ["w"],
    "v": ["s"],
    "w": ["v"],
    "t": ["w", "x"],
    "x": ["x"]
}

colors, parents, times  = dfs(graph, "r")

format_table(colors, "Colors")
format_table(times, "Times")
format_table(parents, "Parents")