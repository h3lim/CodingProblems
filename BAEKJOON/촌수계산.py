import sys
from collections import deque

N = int(sys.stdin.readline())

rel1,rel2 = map(int,sys.stdin.readline().split())

num = int(sys.stdin.readline())

rel =[[] for _ in range(N+1)]

for i in range(num):
    tmp1,tmp2 = map(int,sys.stdin.readline().split())
    rel[tmp1].append(tmp2)
    rel[tmp2].append(tmp1)

def bfs(rel1,rel2):
    visited = set()

    dq = deque([(rel1, 0)])

    while dq:
        r, n = dq.popleft()
        if r == rel2:
            return n

        for i in rel[r]:
            if i not in visited:
                dq.append((i,n+1))
                visited.add(i)

    return -1
ans = bfs(rel1,rel2)
print(ans)

