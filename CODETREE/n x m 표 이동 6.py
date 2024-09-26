from collections import deque

n, m, t = map(int, input().split())

board = []

for i in range(n):
    board.append(list(map(int, input().split())))

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

dq = deque()
visited = set()
dq.append((0, 0, 0))
visited.add((0, 0))

ans = float("inf")
twoD = float("inf")
while dq:
    x, y, d = dq.popleft()
    if x == n - 1 and y == m - 1:
        ans = d

    for dx, dy in dir:
        newX, newY = x + dx, y + dy

        if newX < 0 or newX >= n or newY < 0 or newY >= m or board[newX][newY] == 1 or (newX, newY) in visited:
            continue
        if board[newX][newY] == 2:
            twoD = d + 1
        dq.append((newX, newY, d + 1))
        visited.add((newX, newY))

check = 0
twoX, twoY = 0, 0
for i in range(n):
    if check == 1:
        break
    for j in range(m):
        if board[i][j] == 2:
            twoX, twoY = i, j
            check = 1
            break

tD = abs(n - 1 - twoX) + abs(m - 1 - twoY)

twoD = twoD + tD

ans = min(ans, twoD)

if ans == float("inf") or ans > t:
    print("Fail")
else:
    print(ans)