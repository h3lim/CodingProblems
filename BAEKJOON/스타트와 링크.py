import sys
from itertools import combinations
import math
N = int(sys.stdin.readline())

ability = []

for i in range(N):
    ability.append(list(map(int,sys.stdin.readline().split())))

numbers = [n for n in range(N)]

c = []
for combo in combinations(numbers, N//2):
    first = list(combo)
    second = [num for num in numbers if num not in first]
    c.append((first,second))
ans = float("inf")

for a,b in c:
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                sum1 += ability[a[i]][a[j]]
                sum2 +=  ability[b[i]][b[j]]
    ans = min(ans,abs(sum1 -sum2))
print(ans)