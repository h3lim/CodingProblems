def solution(wallpaper):
    ans = [len(wallpaper), len(wallpaper[0]), 0, 0]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                ans[0] = min(ans[0], i)
                ans[1] = min(ans[1], j)
                ans[2] = max(ans[2], i + 1)
                ans[3] = max(ans[3], j + 1)

    return ans