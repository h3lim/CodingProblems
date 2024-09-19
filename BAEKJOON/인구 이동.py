import sys
from collections import deque
import math

N, L, R = map(int,sys.stdin.readline().split())

board = []

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))


dir = [[1,0],[-1,0],[0,1],[0,-1]]


def bfs(i,j):
    dq = deque([(i, j)])
    visited.add((i, j))
    unity = set()
    unitySum = []
    while dq:
        i, j = dq.popleft()
        unity.add((i,j))
        unitySum.append(board[i][j])
        for x,y in dir:
            nextRow, nextCol = i + x, j + y

            if 0 <= nextRow < N and 0 <= nextCol < N and L<= abs(board[i][j] - board[nextRow][nextCol]) <= R and (nextRow,nextCol) not in visited:
                dq.append((nextRow,nextCol))
                visited.add((nextRow,nextCol))

    if len(unity) == 1:
        return 0
    else:
        for x, y in unity:
            board[x][y] = math.floor(sum(unitySum) / len(unity))
        return math.floor(sum(unitySum) / len(unity))
ans = 0

while 1:
    visited = set()
    s = 0
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                s += bfs(i,j)
    if s == 0:
        break
    else:
        ans += 1

print(ans)