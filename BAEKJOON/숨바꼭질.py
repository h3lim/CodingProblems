import sys
from collections import deque

S,B = map(int, sys.stdin.readline().split())
visited = set()
def bfs(S,B):
    dq = deque([S])
    visited = [0] * 10001
    visited[S] = 1
    while 1:
        c = dq.popleft()
        if c == B:
            return visited[c]
        for i in (c + 1, c - 1, c*2):
            if 0 <= i <= 10000 and visited[i] == 0:
                dq.append(i)
                visited[i] = visited[c] + 1
ans = bfs(S,B)
print(ans)