import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

adj_small = [[] for _ in range(N + 1)]
adj_big = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_small[a].append(b)
    adj_big[b].append(a)

def dfs(v, adj, visited):
    count = 0
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            count += 1 + dfs(neighbor, adj, visited)
    return count

answer = 0

for i in range(1, N + 1):
    visited_small = [False] * (N + 1)
    visited_big = [False] * (N + 1)

    small_count = dfs(i, adj_small, visited_small)
    big_count = dfs(i, adj_big, visited_big)

    if small_count + big_count == N - 1:
        answer += 1

print(answer)