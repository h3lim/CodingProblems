import sys
N,M = map(int, sys.stdin.readline().split())

board = []

dir = [[1,0],[-1,0],[0,1],[0,-1]]
ans = float("inf")
def solve(c,h):
    sm = 0

    for h1,h2 in h:
        mn = 2 * N
        for c1,c2 in c:
            mn = min(mn, abs(h1-c1) + abs(h2-c2))
        sm += mn
    return sm
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

chicken,house = [], []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append((i,j))
        if board[i][j] == 1:
            house.append((i,j))

ans = float("inf")

def backtrack(curr,i,lst):
    global ans
    if len(curr) == M:
        ans = min(ans,solve(curr,house))
        return

    for num in range(i, len(lst)):
        curr.append(lst[num])
        backtrack(curr, num+1, lst)
        curr.pop()

backtrack([],0,chicken)
print(ans)