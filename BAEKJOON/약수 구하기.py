import math
N,K = map(int, input().split())

lst = set()
check = 0
for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        if i * i == N:
            lst.append(i)
        else:
            lst.append(i)
            lst.append(N//i)


lst.sort()

if 0 < K <= len(lst):
    print(lst[K-1])
else:
    print(0)





