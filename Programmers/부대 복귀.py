from collections import defaultdict
from collections import deque


def solution(n, roads, sources, destination):
    ans = []
    graph = defaultdict(list)

    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    dq = deque()
    dq.append((destination, 0))
    d = [-1] * (n + 1)
    d[destination] = 0
    while dq:
        place, dist = dq.popleft()

        for i in graph[place]:
            if d[i] == -1:
                d[i] = dist + 1
                dq.append((i, dist + 1))

    for i in sources:
        ans.append(d[i])

    return ans