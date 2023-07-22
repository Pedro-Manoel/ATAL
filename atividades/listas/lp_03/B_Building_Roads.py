from collections import deque

def create_graph(n, m):
    graph = [[] for _ in range(n + 1)]
  
    for _ in range(m):
        vertex1, vertex2 = map(int, input().split())
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    
    return graph

def dfs(graph, vertex, visited):
    queue = deque()
    queue.append(vertex)
    
    while queue:
        vertex = queue.popleft()

        if vertex in visited:
            continue

        visited.add(vertex)

        for adjVertex in graph[vertex]:
            queue.append(adjVertex)
  
def scc(graph, n):
    visited = set()
    connections = []

    for vertex in range(1, n + 1):
        if vertex not in visited:
            connections.append(vertex)
            dfs(graph, vertex, visited)

    return connections

n, m = map(int, input().split())
graph = create_graph(n, m)
connections = scc(graph, n)

print(len(connections) - 1)
for i in range(len(connections) - 1):
    print(connections[i], connections[i + 1])