INF = int(1e9)

v,e = map(int, input().split())

edges = []

distance = [INF] * (v + 1)

for _ in range(e):
    sv,ev,cost = map(int, input().split())
    edges.append((sv,ev,cost))

def bellmanFord(start):
    distance[start] = 0
    for i in range(v):
        for j in range(e):
            currNode, nextNode, edgeCost = edges[j]
            if distance[currNode] != INF and distance[currNode] + edgeCost < distance[nextNode]:
                distance[nextNode] = distance[currNode] + edgeCost

                if i == v - 1:
                    return False

    return True

if bellmanFord(1):
    for i in range(2, v + 1):
        if distance[i] != INF:
            print(distance[i])

else:
    print("A negative cycle exists")
