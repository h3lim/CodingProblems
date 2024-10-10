import heapq
def solution(jobs):
    jobs.sort()
    currTime = 0
    totalTime = 0
    heap = []
    idx = 0

    while idx < len(jobs) or heap:
        while idx < len(jobs) and jobs[idx][0] <= currTime:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if heap:
            processingTime, startTime = heapq.heappop(heap)
            currTime += processingTime
            totalTime += currTime - startTime
        else:
            currTime = jobs[idx][0]

    return totalTime // len(jobs)