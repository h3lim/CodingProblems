from collections import deque


def rotate(shape):
    rotation = []

    for k in range(4):
        rotated = []
        for x, y in shape:
            if k == 0:
                rx, ry = x, y
            elif k == 1:
                rx, ry = y, -x
            elif k == 2:
                rx, ry = -x, -y
            else:
                rx, ry = -y, x

            rotated.append((rx, ry))
        min_x = min(p[0] for p in rotated)
        min_y = min(p[1] for p in rotated)
        normalized = tuple(sorted((x - min_x, y - min_y) for x, y in rotated))
        rotation.append((normalized))

    return list(set(rotation))


def normalize(shape):
    min_x = float("inf")
    min_y = float("inf")

    for x, y in shape:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        normalized = sorted((x - min_x, y - min_y) for x, y in shape)

    return normalized


def find_blank(board, x, y, visited):
    shape = [(x, y)]
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    dq = deque()
    dq.append((x, y))
    visited[x][y] = 1

    while dq:
        x, y = dq.popleft()

        for dx, dy in dir:
            newX, newY = x + dx, y + dy

            if 0 > newX or newX >= len(board) or 0 > newY or newY >= len(board[0]) or visited[newX][newY] == 1 or \
                    board[newX][newY] == 1:
                continue
            visited[newX][newY] = 1
            dq.append((newX, newY))
            shape.append((newX, newY))

    return shape


def find_shape(board, x, y, visited):
    shape = [(x, y)]
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    dq = deque()
    dq.append((x, y))
    visited[x][y] = 1

    while dq:
        x, y = dq.popleft()

        for dx, dy in dir:
            newX, newY = x + dx, y + dy

            if 0 > newX or newX >= len(board) or 0 > newY or newY >= len(board[0]) or visited[newX][newY] == 1 or \
                    board[newX][newY] == 0:
                continue
            visited[newX][newY] = 1
            dq.append((newX, newY))
            shape.append((newX, newY))

    return shape


def solution(game_board, table):
    blank_shape = []

    visited = [[0] * len(game_board[0]) for _ in range(len(game_board))]

    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0 and visited[i][j] != 1:
                blank_shape.append(find_blank(game_board, i, j, visited))

    normalized_blank_shape = []

    for i in blank_shape:
        normalized_blank_shape.append(normalize(i))

    shape = []

    visited = [[0] * len(game_board[0]) for _ in range(len(game_board))]

    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if table[i][j] == 1 and visited[i][j] != 1:
                shape.append(find_shape(table, i, j, visited))

    all_shape = []
    for i in shape:
        all_shape.append(rotate(i))

    used_pieces = [0] * len(all_shape)
    used_blank = [0] * len(normalized_blank_shape)
    ans = 0

    for i, l in enumerate(all_shape):
        for j in l:
            if used_pieces[i] == 0:
                for m, k in enumerate(normalized_blank_shape):
                    if tuple(k) == j and used_blank[m] == 0:
                        used_pieces[i] = 1
                        used_blank[m] = 1
                        ans += len(j)
                        break

    return ans