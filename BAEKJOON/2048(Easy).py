import sys
from collections import deque
import copy
N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

dir = [[1,0], [-1,0], [0,1], [0,-1]]

def moveUp(board, x):
    for i in range(len(board)):
        for j in range(len(board[i])):
            d = x
            while 0 <= i + d <len(board) and (board[i + d][j] == board[i][j] or (board[i+d][j] != 0 and board[i][j] == 0)):
                if board[i + d][j] == board[i][j]:
                    board[i][j] += board[i + d][j]

                elif board[i+d][j] != 0 and board[i][j] == 0:
                    board[i][j] = board[i+d][j]
                board[i+d][j] = 0
                d += 1
        return copy.deepcopy(board)

def moveDown(board,x):
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[i])):
            d = x
            while 0 <= i + d < len(board) and (board[i + d][j] == board[i][j] or (board[i+d][j] != 0 and board[i][j] == 0)):
                if board[i + d][j] == board[i][j]:
                    board[i][j] += board[i + d][j]
                elif board[i+d][j] != 0 and board[i][j] == 0:
                    board[i][j] = board[i+d][j]
                board[i+d][j] = 0
                d -= 1
    return copy.deepcopy(board)
def moveRight(board,y):
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[i])-1, -1, -1):
            d = y
            while  0 <= j + d < len(board[i]) and (board[i][j+d] == board[i][j] or (board[i][j+d] != 0 and board[i][j] == 0)):
                if board[i][j+d] == board[i][j]:
                    board[i][j] += board[i][j+d]

                elif board[i][j+d] != 0 and board[i][j] == 0:
                    board[i][j] = board[i][j+d]
                board[i][j+d] = 0
                d -= 1
        return copy.deepcopy(board)
def moveLeft(board,y):
    for i in range(len(board)):
        for j in range(len(board[i])):
            d = y
            while 0 <= j+d < len(board[i]) and (board[i][j+d] == board[i][j] or (board[i][j+d] != 0 and board[i][j] == 0)):
                if board[i][j+d] == board[i][j]:
                    board[i][j] += board[i][j+d]

                elif board[i][j+d] != 0 and board[i][j] == 0:
                    board[i][j] = board[i][j+d]
                board[i][j+d] = 0
                d += 1
        return copy.deepcopy(board)

def bfs(board):
    ans = 0
    dq = deque()
    for x,y in dir:
        tmp = copy.deepcopy(board)
        if x > 0:
            dq.appendleft(moveUp(tmp, x))
        elif x < 0:
            dq.appendleft(moveDown(tmp, x))
        elif y > 0:
            dq.appendleft(moveLeft(tmp, y))
        else:
            dq.appendleft(moveRight(tmp, y))


    cnt = 0
    while cnt < 1024:
        cnt += 1
        tmp = dq.popleft()

        ans = max(ans, max(max(i) for i in tmp))
        for x, y in dir:
            if x > 0:
                dq.appendleft(moveUp(tmp, x))
            elif x < 0:
                dq.appendleft(moveDown(tmp, x))
            elif y > 0:
                dq.appendleft(moveLeft(tmp, y))
            else:
                dq.appendleft(moveRight(tmp, y))

    return ans


print(bfs(board))