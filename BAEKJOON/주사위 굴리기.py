import sys
from collections import deque

N, M, i, j, k = map(int, sys.stdin.readline().split())

board= [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
order = deque(list(map(int,sys.stdin.readline().split())))

dq = deque([(i,j)])
dice= [0,0,0,0,0,0]
while order:
    d = order.popleft()
    if d == 1:
        if dq[0][1]+1 >= len(board[0]):
            continue
        x,y = dq.popleft()
        tmp1,tmp2,tmp3 = dice[0], dice[2],dice[5]
        dice[0] = dice[4]
        dice[5] = tmp1
        dice[2] =  tmp3
        dice[4] = tmp2
        dq.append((x,y+1))
    elif d == 2:
        if dq[0][1]-1 < 0:
            continue
        x, y = dq.popleft()
        tmp1, tmp2, tmp3 = dice[0], dice[2], dice[4]
        dice[0] = dice[5]
        dice[4] = tmp1
        dice[2] = tmp3
        dice[5] = tmp2
        dq.append((x,y-1))
    elif d== 3:
        if dq[0][0]-1 < 0:
            continue
        x, y = dq.popleft()
        tmp1, tmp2, tmp3 = dice[0], dice[2], dice[1]
        dice[0] = dice[3]
        dice[1] = tmp1
        dice[2] = tmp3
        dice[3] = tmp2
        dq.append((x-1,y))
    else:
        if dq[0][0]+1 >= len(board):
            continue
        x, y = dq.popleft()
        tmp1,tmp2,tmp3 = dice[0], dice[2],dice[3]
        dice[0] = dice[1]
        dice[3] = tmp1
        dice[2] = tmp3
        dice[1] = tmp2
        dq.append((x+1, y))

    if board[dq[0][0]][dq[0][1]] != 0:
        dice[2] = board[dq[0][0]][dq[0][1]]
        board[dq[0][0]][dq[0][1]] = 0
    else:
        board[dq[0][0]][dq[0][1]] = dice[2]
    print(dice[0])

