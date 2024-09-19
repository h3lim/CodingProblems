import sys
from collections import deque
import copy
R,C = map(int,sys.stdin.readline().split())

board = []

for i in range(R):
    board.append(list(sys.stdin.readline().rstrip()))

dir = [[1,0],[-1,0],[0,1],[0,-1]]

v = [[set()  for _ in range(C)] for _ in range(R)]
v[0][0].add(board[0][0])
dq = deque([(0,0,1,board[0][0])])
 
ans = 0
while dq:
    i,j,m,alpha = dq.popleft()
    ans = max(ans,m)
    for x,y in dir:
        nextRow, nextCol = i + x, j + y

        if 0 <= nextRow < R and 0 <= nextCol < C and board[nextRow][nextCol] not in alpha:
            if alpha + board[nextRow][nextCol] not in v[nextRow][nextCol]:
                dq.append((nextRow, nextCol, m + 1, alpha + board[nextRow][nextCol]))
                v[nextRow][nextCol].add((alpha + board[nextRow][nextCol]))

print(ans)

