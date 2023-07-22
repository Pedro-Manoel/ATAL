import heapq

def create_graph(n, m):
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        origin, destiny, weight = map(int, input().split())
        graph[origin].append((destiny, weight))
        
    return graph

def dijkstra(graph, n, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    queue = [(0, start)]

    while queue:
        weight, node = heapq.heappop(queue)
        if weight > dist[node]:
            continue
        for adj, cost in graph[node]:
            if dist[adj] > dist[node] + cost:
                dist[adj] = dist[node] + cost
                heapq.heappush(queue, (dist[adj], adj))
    
    return dist[1:]

n, m = map(int, input().split())
graph = create_graph(n, m)
print(graph)
result = dijkstra(graph, n, 1)
print(*result)