from collections import Counter
import heapq


def solution(k, tangerine):
    cnt = Counter(tangerine)

    hq = []
    for i, v in cnt.items():
        heapq.heappush(hq, (-v, i))

    ans = 0

    while k > 0:
        mx, n = heapq.heappop(hq)
        if k + mx >= 0:
            k += mx
            ans += 1
        else:
            ans += 1
            break
    return ans