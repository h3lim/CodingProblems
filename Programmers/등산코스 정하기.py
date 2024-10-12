from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    hq = []
    dist = [float('inf')] * (n + 1)
    setSummit = set(summits)

    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    for i in gates:
        heapq.heappush(hq, (0, i))
        dist[i] = 0

    while hq:
        currDist, currNd = heapq.heappop(hq)

        if currDist > dist[currNd] or currNd in setSummit:
            continue

        for i, v in graph[currNd]:
            curr_intensity = max(currDist, v)
            if curr_intensity < dist[i]:
                dist[i] = curr_intensity
                heapq.heappush(hq, (curr_intensity, i))

    result_summit = float('inf')
    result_intensity = float('inf')
    for summit in sorted(summits):
        if dist[summit] < result_intensity:
            result_summit = summit
            result_intensity = dist[summit]

    return [result_summit, result_intensity]