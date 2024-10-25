def find_min_change(x,y,color):
    cnt = 0
    if color == "B":
        for i in range(x, x+8):
            for j in range(y,y+8):
                if i % 2 == 0:
                    if j % 2 == 0 and board[i][j] != "B":
                        cnt += 1
                    elif j % 2 == 1 and board[i][j] != "W":
                        cnt += 1
                else:
                    if j % 2 == 0 and board[i][j] != "W":
                        cnt += 1
                    elif j % 2 == 1 and board[i][j] != "B":
                        cnt += 1
    else:
        for i in range(x,x+8):
            for j in range(y,y+8):
                if i % 2 == 0:
                    if j % 2 == 0 and board[i][j] != "W":
                        cnt += 1
                    elif j % 2 == 1 and board[i][j] != "B":
                        cnt += 1
                else:
                    if j % 2 == 0 and board[i][j] != "B":
                        cnt += 1
                    elif j % 2 == 1 and board[i][j] != "W":
                        cnt += 1
    return cnt

N,M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(input()))


ans = float("inf")

for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, find_min_change(i,j,"B"))
        ans = min(ans, find_min_change(i,j,"W"))

print(ans)