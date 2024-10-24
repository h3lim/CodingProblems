N,M = map(int, input().split())
s1 = set()
s2 = set()

for _ in range(N):
    s1.add(input())
for _ in range(M):
    s2.add(input())

s = s1.intersection(s2)
lst = list(s)
lst.sort()
print(len(lst))

for i in range(len(lst)):
    print(lst[i])

