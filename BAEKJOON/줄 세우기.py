from collections import deque

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


dq = deque()

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        dq.append(i)

result = []
while dq:
    now = dq.popleft()

    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            dq.append(i)

for i in result:
    print(i, end = " ")