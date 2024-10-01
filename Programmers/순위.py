def solution(n, results):
    INF = float('inf')
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for w, l in results:
        graph[w][l] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    ans = 0

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] != float("inf") or graph[j][i] != float("inf"):
                cnt += 1

        if cnt == n:
            ans += 1

    return ans