def solution(n, computers):
    def dfs(nd, visited):
        visited.add(nd)

        for i, v in enumerate(computers[nd]):
            if i not in visited and v == 1:
                dfs(i, visited)

    visited = set()
    ans = 0

    for i in range(n):
        if i not in visited:
            ans += 1
            dfs(i, visited)

    return ans
