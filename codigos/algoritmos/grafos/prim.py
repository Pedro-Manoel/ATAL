import heapq

def prim(graph, start):
    visited = set([start])
    min_heap = []
    mst = []
    cost = 0

    for adj, weight in graph[start].items():
        heapq.heappush(min_heap, (weight, start, adj))

    while min_heap:
        weight, source, destination = heapq.heappop(min_heap)

        if destination not in visited:
            mst.append((source, destination, weight))
            visited.add(destination)
            cost += weight

            for adj, weight in graph[destination].items():
                heapq.heappush(min_heap, (weight, destination, adj))

    return (mst, cost)

# Example
graph = {
    "a": {"b": 4, "h": 8},
    "b": {"a": 4, "c": 8, "h": 11},
    "c": {"b": 8, "d": 7, "f": 4, "i": 2},
    "d": {"c": 7, "e": 9, "f": 14},
    "e": {"d": 9, "f": 10},
    "f": {"c": 4, "d": 14, "e": 10, "g": 2},
    "g": {"f": 2, "h": 1, "i": 6},
    "h": {"a": 8, "b": 11, "g": 1, "i": 7},
    "i": {"c": 2, "g": 6, "h": 7}
}

minimum_spanning_tree, cost = prim(graph, "a")

print(f'\nCost: {cost}')
for edge in minimum_spanning_tree:
    source, destination, weight = edge
    print(f'{source} -- {destination} : {weight}')
