def solution(park, routes):
    x, y = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j

    for i in routes:
        direct, dist = i[0], int(i[2:])

        if direct == "E" and y + dist < len(park[0]):
            check = 1
            for j in range(1, dist + 1):
                if park[x][y + j] == "X":
                    check = 0
                    break

            if check == 1:
                x, y = x, y + dist
        elif direct == "S" and x + dist < len(park):
            check = 1
            for j in range(1, dist + 1):
                if park[x + j][y] == "X":
                    check = 0
                    break

            if check == 1:
                x, y = x + dist, y
        elif direct == "W" and y - dist >= 0:
            check = 1
            for j in range(1, dist + 1):
                if park[x][y - j] == "X":
                    check = 0
                    break

            if check == 1:
                x, y = x, y - dist
        elif direct == "N" and x - dist >= 0:
            check = 1
            for j in range(1, dist + 1):
                if park[x - j][y] == "X":
                    check = 0
                    break

            if check == 1:
                x, y = x - dist, y
    return [x, y]