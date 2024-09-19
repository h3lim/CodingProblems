def solution(k, dungeons):
    def dfs(i, s, stamina, curr):
        print(dungeons[i])
        nonlocal ans
        ans = max(ans, curr)

        for j in range(len(dungeons)):
            if j in s:
                continue
            elif dungeons[j][0] <= stamina:
                curr += 1
                s.add(j)
                stamina -= dungeons[j][1]
                dfs(0, s.copy(), stamina, curr)

    ans = 0
    stamina = k
    for i in range(len(dungeons)):
        s = set()
        dfs(i, s.copy(), stamina, 0)

solution(80,[[80,20],[50,40],[30,10]])