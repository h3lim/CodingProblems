from collections import deque
def solution(maps):
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dq = deque()
    dq.append((0, 0, 1))
    visited = set()
    visited.add((0, 0))

    while dq:
        x, y, c = dq.popleft()

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return c

        for dx, dy in dir:
            newX, newY = x + dx, y + dy

            if 0 <= newX < len(maps) and 0 <= newY < len(maps[0]) and maps[newX][newY] == 1 and (
            newX, newY) not in visited:
                dq.append((newX, newY, c + 1))
                visited.add((newX, newY))

    return -1

