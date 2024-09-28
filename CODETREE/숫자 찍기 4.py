n = int(input())


board = [[0 for _ in range(n)] for _ in range(n)]

dir = [[0, 1], [1, 0],[0, -1],[-1, 0]]

for i in range(n):
    board[0][i] = i + 1
dec = n-1
d = 0
num = n+1
row, col = 0, n-1

while num <= n*n:
    for i in range(2):
        if num > n*n:
            break
        d = (d + 1) % 4
        for j in range(dec):
            row, col = row + dir[d][0], col + dir[d][1]
            board[row][col] = num
            num += 1
            if num > n*n:
                break
    dec -= 1

for row in board:
    print(' '.join(map(str, row)))