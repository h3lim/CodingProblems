import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

startX,startY,d = map(int,sys.stdin.readline().split())

board = []

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

dir = [[-1,0],[0,1],[1,0],[0,-1]]


def robotVaucum(curr, ans,d):
    i, j = curr[0][0], curr[0][1]
    while True:
        if board[i][j] == 0:
            ans += 1
            board[i][j] = 2

        allClean = 1

        while allClean == 1:
            for k in ((d + 3) % 4, (d + 2) % 4, (d + 1) % 4, d):
                nextR, nextC = i + dir[k][0], j + dir[k][1]
                if board[nextR][nextC] == 0:
                    i, j, d = nextR, nextC, k
                    allClean = 0
                    break

            else:
                if board[i - dir[d][0]][j - dir[d][1]] == 1:
                        return ans
                else:
                    i,j = i - dir[d][0], j - dir[d][1]

ans = robotVaucum([(startX,startY)], 0, d)

print(ans)