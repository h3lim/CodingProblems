from collections import deque

N = int(input())
result = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = [0] * (N + 1)

for i in range(1, N + 1):
    l = list(map(int, input().split()))
    if len(l) == 2:
        time[i] = l[0]
    elif len(l) >= 3:
        time[i] = l[0]
        j = 1
        while l[j] != -1:
            graph[l[j]].append(i)
            indegree[i] += 1
            j += 1

result = time.copy()

dq = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        dq.append(i)

while dq:
    now = dq.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + time[i])
        if indegree[i] == 0:
            dq.append(i)

for i in range(1, len(result)):
    print(result[i])
