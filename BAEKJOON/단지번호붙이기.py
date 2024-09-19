import sys
from collections import deque

N = int(sys.stdin.readline())

board = []

for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

dir = [[1,0],[-1,0],[0,1],[0,-1]]

visited = set()


def bfs(i,j):
    dq = deque([(i,j)])
    visited.add((i,j))
    area = 0
    while dq:
        i,j = dq.popleft()
        area += 1
        for x,y in dir:
            nextRow, nextCol = i+x, j + y

            if 0 <= nextRow < N and 0 <= nextCol < N and board[nextRow][nextCol] == "1" and (nextRow,nextCol) not in visited:
                dq.append((nextRow,nextCol))
                visited.add((nextRow,nextCol))

    return area

ans = []

for i in range(N):
    for j in range(N):
        if board[i][j] == "1" and (i,j) not in visited:
            num = bfs(i,j)
            ans.append(num)

print(len(ans))
ans.sort()

for i in ans:
    print(i)