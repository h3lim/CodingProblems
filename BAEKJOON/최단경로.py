import heapq

V, E = map(int, input().split())
start = int(input())

cost = [float("INF")] * (V+1)

graph =[[] for _ in range(V+1)]

for i in range(E):
    s,r,c = map(int, input().split())
    graph[s].append((c,r))

visited = [0] * (V+1)
hq = []
heapq.heappush(hq,(0, start))
cost[start] = 0

while hq:
    currC, currL = heapq.heappop(hq)

    if cost[currL] < currC:
        continue
    if visited[currL] == 1:
        continue
    visited[currL] = 1

    for i in graph[currL]:
        candidate = i[0] + currC

        if candidate < cost[i[1]]:
            cost[i[1]] = candidate

            heapq.heappush(hq,(candidate, i[1]))

for i in range(1,len(cost)):
    print(cost[i])