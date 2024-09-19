from collections import deque

def solution(land):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    col = [0] * len(land[0])

    def bfs(i, j, visited):
        dq = deque([(i,j)])
        visited.add((i, j))
        n = 0
        c = set()
        c.add(j)
        while dq:
            i, j = dq.popleft()
            n += 1
            for x, y in dir:
                nextR, nextC = i + x, j + y
                if 0 <= nextR < len(land) and 0 <= nextC < len(land[0]) and (nextR, nextC) not in visited and \
                        land[nextR][nextC] == 1:
                    dq.append((nextR, nextC))
                    visited.add((nextR,nextC))
                    c.add(nextC)

        return n, c

    visited = set()
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 1 and (i, j) not in visited:
                n, c = bfs(i, j, visited)
                for k in c:
                    col[k] = col[k] + n

    return max(col)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))