import heapq

n = int(input())

lst = list(map(int, input().split()))

ans = 0
curr = 0
heapq.heapify(lst)

while lst:
    curr += heapq.heappop(lst)
    ans += curr

print(ans)

