def solution(n, costs):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    total_cost = 0
    edges = []
    for a, b, c in costs:
        edges.append((c, a, b))

    edges.sort()

    for i in range(len(costs)):
        c, a, b = edges[i]

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += c
    return total_cost