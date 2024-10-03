import math

N = int(input())
ans = 0
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

coordinates = []

for i in range(N):
    coordinates.append(list(map(float, input().split())))

edges = []

for i in range(N):
    for j in range(i+1, N):
        cost = math.sqrt((abs(coordinates[j][0]-coordinates[i][0])**2) + (abs(coordinates[j][1]-coordinates[i][1])**2))
        edges.append((cost,i,j))

edges.sort()

parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

for edge in edges:
    c,a,b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        ans += c

print(round(ans,2))