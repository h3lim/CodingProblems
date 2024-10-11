import heapq
def prim(graph, start):
    # 우선순위 큐와 방문 배열 초기화
    mst_cost = 0
    visited = [False] * len(graph)
    pq = [(0, start)]  # (간선의 가중치, 시작 정점)으로 우선순위 큐 초기화

    while pq:
        weight, node = heapq.heappop(pq)

        # 이미 방문한 노드는 무시
        if visited[node]:
            continue

        # 노드를 MST에 추가하고 비용 갱신
        visited[node] = True
        mst_cost += weight

        # 현재 노드에서 갈 수 있는 모든 노드를 탐색
        for next_node, edge_weight in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (edge_weight, next_node))

    return mst_cost
graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}

start_node = 0
mst_cost = prim(graph, start_node)
print("Minimum Spanning Tree Cost:", mst_cost)