import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())

board = []

dir = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

visited = set()
dq = deque([(0,0,1)])
visited.add((0,0))
ans = 0

while dq:
    i,j,m = dq.popleft()

    if i == N-1 and j == M-1:
        ans = m
        break


    for x,y in dir:
        nextRow,nextCol = i + x, j + y

        if 0 <= nextRow < N and 0 <= nextCol < M and board[nextRow][nextCol] == "1" and (nextRow, nextCol) not in visited:
            dq.append((nextRow,nextCol, m+1))
            visited.add((nextRow,nextCol))


print(ans)