import sys
import copy
N, M = map(int, sys.stdin.readline().split())

board = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

tetromino =[[(0,1), (0,2), (0,3)],[(1,0), (2,0), (3,0)], # ㅣ(회전)
	[(0,1), (1,0), (1,1)],
    [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], [(0,1), (1,1), (2,1)], [(0,1), (0,2),(-1,2)], # ㄴ(회전)
    [(0,1),(-1,1),(-2,1)], [(1,0), (1,1), (1,2)], [(0,1), (1,0), (2,0)], [(0,1), (0,2), (1,2)], # ㄴ대칭(회전)
    [(1,0), (1,1), (2,1)], [(0,1),(-1,1),(-1,2)],   # ㄹ(회전)
    [(1,0), (0,1),(-1,1)], [(0,1), (1,1), (1,2)],   # ㄹ대칭(회전)
    [(0,1), (0,2), (1,1)], [(-1,1),(0,1), (1,1)], [(0,1), (0,2),(-1,1)], [(1,0), (2,0), (1,1)]]

def checkMax(x,y,lst):
    s = board[x][y]
    for p,q in lst:
        if 0 <= x+ p < N and 0 <= y + q < M:
            s += board[x+ p][y + q]
        else:
            return 0
    return s

ans = 0
for x in range(N):
    for y in range(M):
        for t in tetromino:
            ans = max(ans, checkMax(x,y,t))

print(ans)

