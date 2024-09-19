import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
board = []
virusIndex = set()
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
zeroIndex = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zeroIndex.append((i,j))
        if board[i][j] == 2:
            virusIndex.add((i,j))
CNT = len(zeroIndex)
def bfs(wallx1,wally1,wallx2,wally2,wallx3,wally3):
    visited = set()
    cnt = CNT
    cnt -= 3
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    dq = deque()
    board[wallx1][wally1],board[wallx2][wally2],board[wallx3][wally3] = 1,1,1
    for x,y in virusIndex:
        dq.append((x,y))
        visited.add((x,y))
        while dq:
            x1,y1 = dq.popleft()
            for dx,dy in dir:
                nextRow = x1+dx
                nextCol = y1+dy
                if 0 <= nextRow < N and 0 <= nextCol < M and board[nextRow][nextCol] == 0 and (nextRow, nextCol) not in visited:
                    dq.append((nextRow,nextCol))
                    visited.add((nextRow,nextCol))
                    cnt -= 1
    board[wallx1][wally1], board[wallx2][wally2], board[wallx3][wally3] = 0, 0, 0
    return cnt
ans = 0

for i in range(len(zeroIndex)-2):
    for j in range(i+1,len(zeroIndex)-1):
        for k in range(j+1,len(zeroIndex)):
            ans = max(ans,bfs(zeroIndex[i][0], zeroIndex[i][1], zeroIndex[j][0], zeroIndex[j][1], zeroIndex[k][0], zeroIndex[k][1]))


print(ans)
