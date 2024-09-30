from collections import defaultdict
import sys
def solution(n, lighthouse):
    sys.setrecursionlimit(1 << 15)
    dic = defaultdict(list)
    for i, j in lighthouse:
        dic[i].append(j)
        dic[j].append(i)

    visited = [0] * (n + 1)
    dp = [[0, 0] for _ in range(n + 1)]

    def dfs(u):
        visited[u] = 1
        dp[u][0] = 0
        dp[u][1] = 1

        for v in dic[u]:
            if visited[v] == 0:
                dfs(v)
                dp[u][0] += dp[v][1]
                dp[u][1] += min(dp[v][0], dp[v][1])

    dfs(1)

    return min(dp[1][0], dp[1][1])
