ans = 0

N = int(input())
M = int(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
for i in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))


edges.sort()

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent, a, b)
        ans += c

print(ans)