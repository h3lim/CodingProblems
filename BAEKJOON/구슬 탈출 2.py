import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
board = []

dir = [[1,0],[-1,0],[0,1],[0,-1]]

for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

def rolling(rX,rY,bX,bY,x,y,b):
    tmp = copy.deepcopy(b)
    tmpRx, tmpRy = rX,rY
    tmpBx, tmpBy = bX, bY
    passedB = 0
    passedR = 0
    goalR = 0
    goalB = 0
    while tmp[rX+x][rY+y] != "#":
        if tmp[rX+x][rY+y] == "O":
            rX += x
            rY += y
            gaolR = 1
            break
        elif tmp[rX+x][rY+y] == "B":
            passedB = 1
            rX += x
            rY += y
        elif tmp[rX+x][rY+y] == ".":
            rX += x
            rY += y

    while tmp[bX+x][bY+y] != "#":
        if tmp[bX+x][bY+y] == "O":
            bX += x
            bY += y
            goalB = 1
            break
        elif tmp[bX+x][bY+y] == "R":
            passedR = 1
            bX += x
            bY += y
        elif tmp[bX+x][bY+y] == ".":
            bX += x
            bY += y

    if passedB == 1 and goalR == 0:
            rX -= x
            rY -= y
    if passedR == 1 and goalB == 0:
            bX -= x
            bY -= y

    tmp[tmpRx][tmpRy] = "."
    tmp[tmpBx][tmpBy] = "."
    tmp[rX][rY] = "R"
    tmp[bX][bY] = "B"


    return rX,rY,bX,bY,tmp

def bfs(rX,rY,bX,bY, gX,gY):
    dq = deque()
    b = copy.deepcopy(board)

    dq.append((rX,rY,bX,bY, 0, b))
    visited = set()
    visited.add((rX, rY,bX,bY))

    while dq:
        currRx, currRy, currBx, currBy, move, currB = dq.popleft()
        if move >= 10:
            return -1
        for x,y in dir:
            nextRx, nextRy, nextBx, nextBy, nextB = rolling(currRx,currRy,currBx, currBy,x,y,currB)
            if (nextRx,nextRy,nextBx,nextBy) in visited:
                continue
            if (nextRx == gX and nextRy == gY) and (nextBx != gX or nextBy != gY):
                return move + 1

            visited.add((nextRx, nextRy, nextBx, nextBy))
            dq.append((nextRx, nextRy, nextBx, nextBy,move+1,nextB))

    return -1
rX,rY,bX,bY, gX,gY = 0,0,0,0,0,0
R,B,G = 0,0,0
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rX,rY = i, j
            R = 1
        elif board[i][j] == "B":
            bX,bY = i,j
            B = 1
        elif board[i][j] == "O":
            gX,gY = i,j
            G = 1

    if R == 1 and B == 1 and G == 1:
        break

print(bfs(rX, rY, bX, bY, gX, gY))

