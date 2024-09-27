from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    grid = [[-1] * 102 for _ in range(102)]

    for rect in rectangle:
        x1, y1, x2, y2 = [i * 2 for i in rect]
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                grid[x][y] = 0

    for rect in rectangle:
        x1, y1, x2, y2 = [i * 2 for i in rect]
        for x in range(x1, x2 + 1):
            if grid[x][y1] != 0:
                grid[x][y1] = 1
            if grid[x][y2] != 0:
                grid[x][y2] = 1
        for y in range(y1, y2 + 1):
            if grid[x1][y] != 0:
                grid[x1][y] = 1
            if grid[x2][y] != 0:
                grid[x2][y] = 1

    visited = [[0] * 102 for _ in range(102)]
    dq = deque()
    dq.append((characterX * 2, characterY * 2, 0))
    visited[characterX * 2][characterY * 2] = 1

    while dq:
        x, y, d = dq.popleft()

        if x == itemX * 2 and y == itemY * 2:
            return d // 2

        for dx, dy in dir:
            nextX, nextY = x + dx, y + dy

            if 0 > nextX or 102 <= nextX or 0 > nextY or 102 <= nextY or visited[nextX][nextY] == 1 or grid[nextX][
                nextY] != 1:
                continue

            dq.append((nextX, nextY, d + 1))
            visited[nextX][nextY] = 1

    return 0