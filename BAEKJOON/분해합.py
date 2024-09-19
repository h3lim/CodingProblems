import sys

N = int(sys.stdin.readline())

ans = 0
for i in range(N-1,-1,-1):
    if i + sum(list(map(int,str(i)))) == N:
        ans = i

print(ans)