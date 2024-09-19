from collections import deque
for test_case in range(1, 11):
    num = int(input())

    board = []

    for i in range(16):
        board.append((list(map(int,list(input())))))
    dir = [[1,0],[-1,0],[0,1],[0,-1]]

    dq = deque()
    visited = set()
    start = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                dq.append((i,j))
                visited.add((i,j))
                start = 1
                break
        if start == 1:
            break
    success = 0
    while dq:
        x,y = dq.popleft()

        if board[x][y] == 3:
            success = 1
            break

        for dx,dy in dir:
            nextRow, nextCol = x+ dx, y+dy

            if 0 <= nextRow < len(board) and 0 <= nextCol < len(board[0]) and board[nextRow][nextCol] != 1 and (nextRow,nextCol) not in visited:
                visited.add((nextRow, nextCol))
                dq.append((nextRow,nextCol))

    print("#{} {}".format(test_case, success))