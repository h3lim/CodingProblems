import sys

N = int(sys.stdin.readline())
consulting = []
for i in range(N):
    t,p = map(int, sys.stdin.readline().split())
    consulting.append((t,p))

ans = 0
def dfs(i,cost):
    global ans
    ans = max(cost, ans)
    if i == N:
        return
    curr = consulting[i][0]
    j = 0
    while curr+i+j <= N:
        dfs(curr+i+j, cost + consulting[i][1])
        j += 1

for i in range(N):
    dfs(i,0)

print(ans)