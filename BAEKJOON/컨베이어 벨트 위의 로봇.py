import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

num = list(map(int,sys.stdin.readline().split()))


belt = []
for i in range(len(num)):
        belt.append(num[i])


robot = [0] * N

ans = 0

while 1:
    ans += 1

    robot = [0] + robot[:-1]
    belt = [belt[-1]] + belt[:-1]
    robot[N - 1] = 0

    for i in range(N - 2, 0, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            belt[i + 1] -= 1

    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    if belt.count(0) >= K:
        break
print(ans)