from collections import deque

def dijkstra(dq):
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    while dq:
        x, y = dq.popleft()

        for dx,dy in dir:
            nextRow, nextCol = x + dx, y + dy

            if 0 <= nextRow < n and 0 <= nextCol < n:
                if dist[nextRow][nextCol] >  dist[x][y] + board[nextRow][nextCol]:
                    dist[nextRow][nextCol] = dist[x][y] + board[nextRow][nextCol]
                    dq.append((nextRow,nextCol))

N = int(input())
for i in range(N):
    n = int(input())

    board = [list(map(int, list(input()))) for _ in range(n)]
    dist = [[float("inf") for _ in  range(n)] for _ in range(n)]


    dist[0][0] = 0
    dq = deque()
    dq.append((0,0))

    dijkstra(dq)
    print("#{} {}".format(i+1, dist[n-1][n-1]))





