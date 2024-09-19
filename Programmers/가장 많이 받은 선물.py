def solution(friends, gifts):
    ans = dict()
    d = dict()
    est = dict()

    for i in friends:
        d[i] = dict()
        est[i] = 0
        ans[i] = 0

    for i in gifts:
        g, r = map(str, i.split())
        if r not in d[g]:
            d[g][r] = 1
        else:
            d[g][r] += 1
        est[g] += 1
        est[r] -= 1

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if i != j:
                if friends[j] in d[friends[i]] and friends[i] in d[friends[j]]:
                    if d[friends[i]][friends[j]] > d[friends[j]][friends[i]]:
                        ans[friends[i]] += 1
                    elif d[friends[i]][friends[j]] < d[friends[j]][friends[i]]:
                        ans[friends[j]] += 1
                    else:
                        if est[friends[i]] > est[friends[j]]:
                            ans[friends[i]] += 1
                        elif est[friends[i]] < est[friends[j]]:
                            ans[friends[j]] += 1
                elif friends[j] in d[friends[i]]:
                    ans[friends[i]] += 1
                elif friends[i] in d[friends[j]]:
                    ans[friends[j]] += 1
                else:
                    if est[friends[i]] > est[friends[j]]:
                        ans[friends[i]] += 1
                    elif est[friends[i]] < est[friends[j]]:
                        ans[friends[j]] += 1

    return max(ans.values())