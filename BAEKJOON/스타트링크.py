import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

def bfs(S):
    visited = set()

    dq = deque([(S, 0)])
    visited.add(S)
    ans = 0
    while dq:
        curr, m = dq.popleft()
        if curr == G:
            return m


        for e in (U, -D):
            nextF = curr + e
            if 1 <= nextF <= F and nextF not in visited:
                dq.append((nextF, m + 1))
                visited.add(nextF)
    return -1


ans = bfs(S)

if ans == -1:
    print("use the stairs")
else:
    print(ans)