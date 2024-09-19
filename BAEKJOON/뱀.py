import sys
from collections import deque

N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
turn = deque()
theNumOfApple = int(sys.stdin.readline())

for i in range(theNumOfApple):
    x,y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

theNumOfTurn = int(sys.stdin.readline())

for i in range(theNumOfTurn):
    n, d = map(str, sys.stdin.readline().split())
    turn.append([int(n),d])
ans = 0
dir = [0,1]
body = set()
dq = deque([(0,0)])
body.add((0,0))
cnt = 0

n, d = turn.popleft()

while True:
    cnt += 1
    i,j = dq.popleft()

    if i+dir[0] < 0 or i+dir[0] >= N or j+dir[1] < 0 or j+dir[1] >= N:
        ans = cnt
        break

    if board[i+dir[0]][j+dir[1]] == 1:
        board[i+dir[0]][j+dir[1]] = 0
        dq.appendleft((i,j))
        dq.appendleft((i+dir[0],j+dir[1]))
    else:
        if dq:
            tmpX, tmpY = dq.pop()
            body.remove((tmpX,tmpY))
        dq.appendleft((i,j))
        dq.appendleft((i + dir[0], j + dir[1]))

    if (i+dir[0], j+dir[1]) in body:
        ans = cnt
        break
    body.add((i+dir[0], j+dir[1]))
    if cnt == n:
        if d == "D":
            if dir == [0,1]:dir = [1,0]
            elif dir == [1,0]: dir = [0,-1]
            elif dir == [0,-1]: dir = [-1,0]
            elif dir == [-1,0]: dir = [0,1]

        if d == "L":
            if dir == [0,1]: dir = [-1,0]
            elif dir == [-1,0]: dir = [0,-1]
            elif dir == [0,-1]: dir = [1,0]
            elif dir == [1,0]: dir = [0,1]
        if turn:
            n,d = turn.popleft()

print(ans)


