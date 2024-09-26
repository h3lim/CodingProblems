from collections import defaultdict
import heapq


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 2배로 확대하여 정밀도를 높입니다
    MAX = 102
    field = [[0] * MAX for _ in range(MAX)]

    # 직사각형 그리기
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 2
                elif field[i][j] != 2:
                    field[i][j] = 1

    # 그래프 생성
    graph = defaultdict(list)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(MAX):
        for y in range(MAX):
            if field[x][y] == 1:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < MAX and 0 <= ny < MAX and field[nx][ny] == 1:
                        graph[(x, y)].append((nx, ny))

    # 다익스트라 알고리즘
    def dijkstra(start, end):
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distances[current_node]:
                continue

            if current_node == end:
                return current_distance

            for neighbor in graph[current_node]:
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return -1  # 경로가 없는 경우

    # 시작점과 도착점의 좌표를 2배로 확대
    start = (characterX, characterY)
    end = (itemX, itemY)

    # 최단 거리 계산 및 반환 (2로 나누어 원래 크기로 변환)
    return dijkstra(start, end) // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))