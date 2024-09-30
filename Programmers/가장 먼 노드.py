from collections import defaultdict
from collections import deque


def solution(n, edge):
    dic = defaultdict(list)

    for i, j in edge:
        dic[i].append(j)
        dic[j].append(i)

    def bfs(u):
        dq = deque()
        dq.append((u, 0))
        visited[u] = 1
        while dq:
            v, d = dq.popleft()
            dist[v] = max(dist[v], d)

            for c in dic[v]:
                if visited[c] == 0:
                    visited[c] = 1
                    dq.append((c, d + 1))

    dist = [0] * (n + 1)

    visited = [0] * (n + 1)
    bfs(1)

    ans = 0
    mx = max(dist)

    for i in range(1, len(dist)):
        if mx == dist[i]:
            ans += 1

    return ans