from collections import deque
N = int(input())

lst = deque(i for i in range(1,N+1))
cnt = 0

while len(lst) > 1:
    tmp = lst.popleft()
    if cnt % 2 == 1:
        lst.append(tmp)
    cnt += 1

print(lst[0])