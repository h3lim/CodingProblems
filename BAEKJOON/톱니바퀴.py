import sys
from collections import deque

gears = []
for i in range(4):
    gears.append(list(sys.stdin.readline().rstrip()))

num = int(sys.stdin.readline())

rotation = []

for i in range(num):
    rotation.append(map(int,sys.stdin.readline().split()))
def solve(g,dir):
    lst = [0] * 4
    d = dir
    lst[g] = d
    for i in range(g+1, len(gears)):
        if gears[i-1][2] != gears[i][6]:
            if dir == 1:
                lst[i] = -1
                dir = -1
            else:
                lst[i] = 1
                dir = 1
        else:
            break

    dir = d
    for i in range(g-1,-1,-1):
        if gears[i+1][6] != gears[i][2]:
            if dir == 1:
                lst[i] = -1
                dir = -1
            else:
                lst[i] = 1
                dir = 1
        else:
            break
    for i in range(len(lst)):
        if lst[i] == 1:
            gears[i] = [gears[i][-1]] + gears[i][:-1]
        elif lst[i] == -1:
            gears[i] = gears[i][1:]+[gears[i][0]]


for n,d in rotation:
    solve(n-1,d)

ans = 0

for k in range(4):
    if gears[k][0] == "1":
        ans += 2**k

print(ans)
