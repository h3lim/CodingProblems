from collections import defaultdict
from collections import deque

ans = []
N,M = map(int,input().split())

dic = defaultdict(list)

indegree = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    dic[a].append(b)
    indegree[b] += 1

dq = deque()

for i in range(1,len(indegree)):
    if indegree[i] == 0:
        dq.append(i)


while dq:
    p = dq.popleft()
    ans.append(p)

    for i in dic[p]:
        indegree[i] -= 1

        if indegree[i] == 0:
            dq.append(i)

for i in ans:
    print(i, end = " ")