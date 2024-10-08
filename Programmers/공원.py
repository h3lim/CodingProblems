def solution(mats, park):
    ans = -1
    mats.sort(reverse=True)

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "-1":
                for k in mats:
                    if i + k - 1 < len(park) and j + k - 1 < len(park[i]):
                        check = 1
                        for l in range(k):
                            if not (len(set(park[i + l][j:j + k])) == 1 and "-1" in set(park[i + l][j:j + k])):
                                check = 0
                                break
                        if check == 1:
                            ans = max(ans, k)

    return ans
