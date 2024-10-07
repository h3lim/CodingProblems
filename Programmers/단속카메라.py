def solution(routes):
    ans = 0
    routes.sort()
    i = 0

    while i < len(routes):
        next = i + 1
        if next < len(routes):
            while next < len(routes) and routes[i][1] >= routes[next][0]:
                next += 1

        ans += next - i -1
        i = next

    return ans

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])