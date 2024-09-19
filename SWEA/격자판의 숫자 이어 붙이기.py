from collections import deque

T = int(input())

def bfs(dq):
    while dq:
        x,y,s,d = dq.popleft()

        if d == 7:
            ans.add(s)

        if d < 7:
            for dx, dy in dir:
                nextRow, nextCol = x + dx, y + dy
                if 0 <= nextRow < 4 and 0 <= nextCol < 4:
                    dq.append((nextRow,nextCol,s + str(board[nextRow][nextCol]), d + 1))


dir = [[1,0],[-1,0],[0,1],[0,-1]]
for n in range(1, T+1):

    board = [list(map(int, input().split())) for _ in range(4)]
    ans = set()
    dq = deque()
    for i in range(4):
        for j in range(4):
            dq.append((i,j,str(board[i][j]),1))
            bfs(dq)

    print("#{} {}".format(n,len(ans)))
