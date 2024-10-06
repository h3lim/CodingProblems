from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for i, j in graph.items():
        j.sort(reverse=True)

    routes = []

    def dfs(city):
        while graph[city]:
            nextArrival = graph[city].pop()
            dfs(nextArrival)
            routes.append(nextArrival)

    dfs("ICN")
    routes.append("ICN")
    return routes[::-1]
