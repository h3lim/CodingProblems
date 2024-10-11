INF = int(1e9)

v,e = map(int, input().split())

edges = []

distance = [INF] * (v + 1)

for _ in range(e):
    sv,ev,cost = map(int, input().split())
    edges.append((sv,ev,cost))


def bellman_ford(graph, start, n):
    distance = [float("inf")] * n
    distance[start] = 0

    for i in range(n - 1):
        for u, v, w in graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] != float("inf") and distance[u] + w < distance[v]:
            print("Negative weight cycle detected.")

            return distance

bellman_ford(edges,1,v)