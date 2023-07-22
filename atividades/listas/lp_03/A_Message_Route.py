from collections import deque

def create_graph(n, m):
  graph = [[] for _ in range(n + 1)]
  
  for _ in range(m):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

  return graph

def bfs(graph, initialVertex, endVertex):
  visited = set()
  queue = deque()
  parent = [None for _ in range(endVertex + 1)]

  visited.add(initialVertex)
  queue.append(initialVertex)
      
  while queue:
    vertex = queue.popleft()
    
    if vertex == endVertex:
      path = [vertex]
      while parent[path[-1]]:
        path.append(parent[path[-1]])
      return path[::-1]
        
    for adj in graph[vertex]:
      if adj not in visited:
        visited.add(adj)
        queue.append(adj)
        parent[adj] = vertex
  
  return []
  
n, m = map(int, input().split())
graph = create_graph(n, m)
path = bfs(graph, 1, n)

if path:
  print(len(path))
  print(*path)
else:
  print("IMPOSSIBLE")