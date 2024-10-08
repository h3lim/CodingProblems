import heapq
def solution(n, works):
    ans = 0
    if sum(works) - n <= 0:
        return 0

    hq = []

    for i in works:
        heapq.heappush(hq, (-i, i))

    while n > 0:
        v = heapq.heappop(hq)[1]
        v -= 1
        heapq.heappush(hq, (-v, v))
        n -= 1

    while hq:
        ans += (heapq.heappop(hq)[1] ** 2)

    return ans