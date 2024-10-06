import heapq
def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        ans += 1
        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, tmp1 + (tmp2 * 2))

    if scoville[0] < K:
        return -1
    return ans