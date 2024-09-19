from collections import deque

N = int(input())

def bfs(dq):
    visited = set()
    visited.add((0,0,0))
    while dq:
        x,y,dx,dy,m = dq.popleft()
        if "0" <=cmmdLst[x][y] <= "9" and (x+dx % r, y+dy % c, m) not in visited:
            dq.append((x + dx % r, y + dy % c, dx, dy, (m + int(cmmdLst[x][y]))))
            visited.add((x + dx % r, y + dy % c, (m + int(cmmdLst[x][y]))))
        elif cmmdLst[x][y] == "." and (x+dx % r, y+dy % c, m) not in visited:
            dq.append((x+dx % r,y+dy % c, dx,dy, m))
            visited.add((x+dx % r,y+dy % c,m))
        elif cmmdLst[x][y] == "v" and (x+1 % r, y % c, m) not in visited:
            dx,dy = 1,0
            dq.append((x + dx % r, y + dy % c, dx, dy, m))
            visited.add((x + dx % r, y + dy % c, m))
        elif cmmdLst[x][y] == ">" and (x+0 % r, y+1 % c, m) not in visited:
            dx,dy = 0,1
            dq.append((x + dx % r, y + dy % c, dx, dy, m))
            visited.add((x + dx % r, y + dy % c, m))
        elif cmmdLst[x][y] == "<" and (x+0 % r, y-1 % c, m) not in visited:
            dx,dy = 0,-1
            dq.append(x + dx % r, y + dy % c, dx, dy, m)
            visited.add((x + dx % r, y + dy % c, m))
        elif cmmdLst[x][y] == "^" and (x-1 % r, y % c, m) not in visited:
            dx,dy = -1,0
            dq.append(x + dx % r, y + dy % c, dx, dy, m)
            visited.add((x + dx % r, y + dy % c, m))
        elif cmmdLst[x][y] == "_" and m == 0 and (x % r, y + 1 % c, m) not in visited:
            dx,dy = 0,1
            dq.append(x + dx % r, y + dy % c, dx, dy, m)
            visited.add((x + dx % r, y + dy % c, m))
        elif cmmdLst[x][y] == "_" and m != 0 and (x % r, y - 1 % c, m) not in visited:
            dx,dy = 0,-1
            dq.append(x + dx % r, y + dy % c, dx, dy, m)
            visited.add((x + dx % r, y + dy % c, m))
        elif cmmdLst[x][y] == "?":
            if (x + 1 % r, y % c, m) not in visited:
                dq.append(x + 1 % r, y % c, 1, 0, m)
                visited.add((x + 1 % r, y % c, m))
            if (x - 1 % r, y % c, m) not in visited:
                dq.append(x - 1 % r, y % c, -1, 0, m)
                visited.add((x - 1 % r, y % c, m))
            if (x % r, y + 1 % c, m) not in visited:
                dq.append(x % r, y + 1 % c, 0, 1, m)
                visited.add((x % r, y + 1 % c, m))
            if (x % r, y-1 % c, m) not in visited:
                dq.append(x % r, y - 1 % c, 0, -1, m)
                visited.add((x + dx % r, y - 1 % c, m))
        elif cmmdLst[x][y] == "@":
            return "YES"
        elif cmmdLst[x][y] == "+" and (x + dx % r, y + dy % c, (m+1) % 16) not in visited:
            dq.append(x + dx % r, y + dy % c, dx, dy, (m+1) % 16)
            visited.add((x + dx % r, y + dy % c, (m+1)%16))
        elif cmmdLst[x][y] == "-":
            if m == 0 and (x + dx % r, y + dy % c, 15) not in visited:
                dq.append(x + dx % r, y + dy % c, dx, dy, 15)
                visited.add((x + dx % r, y + dy % c, 15))
            elif m != 0 and (x + dx % r, y + dy % c, (m-1)) not in visited:
                dq.append(x + dx % r, y + dy % c, dx, dy, m-1)
                visited.add((x + dx % r, y + dy % c, (m - 1)))
    return "NO"
for n in range(1, N + 1):
    r,c = map(int, input().split())
    cmmdLst = []

    for i in range(r):
        cmmdLst.append(list(input()))

    dq = deque()
    dq.append((0,0,0,1,0))
    ans = bfs(dq)
    print("#{} {}".format(n, ans))
