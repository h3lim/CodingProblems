import sys
from collections import deque
import math
C,R,H = map(int,sys.stdin.readline().split())

box = []

for i in range(R*H):
    box.append(list(map(int,sys.stdin.readline().split())))

dir = [[1,0],[-1,0],[0,1],[0,-1],[R,0],[-R,0]]
visited = set()
def bfs(lst):
    dq = deque(lst)
    cnt = 0
    while dq:
        i,j,d = dq.popleft()
        flr = math.floor(i / R)
        cnt = max(cnt,d)
        for x,y in dir:
            nextRow, nextCol = i + x, j + y

            if 0 <= nextRow < R*H and 0 <= nextCol < C and box[nextRow][nextCol] == 0  and (nextRow,nextCol) not in visited:
                if x == 1 or x == -1:
                    if flr != math.floor(nextRow/ R):
                        continue

                box[nextRow][nextCol] = 1
                dq.append((nextRow,nextCol,d+1))
                visited.add((nextRow,nextCol))
    return cnt

ans = 0
ripeTomato = []
for i in range(len(box)):
    for j in range(len(box[i])):
        if box[i][j] == 1:
            ripeTomato.append((i,j,0))

ans = bfs(ripeTomato)
if any(0 in row for row in box):
    print(-1)
else:
    print(ans)