from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    ans = []
    dic = defaultdict(int)
    alpha = set()
    for c in course:
        for o in orders:
            for comb in list(combinations(o, c)):
                dic["".join(sorted(comb))] += 1
                alpha.add("".join(sorted(comb)))

    for i in course:
        tmp = []
        cnt = 2
        for s, c in dic.items():
            if len(s) == i and c == cnt:
                tmp.append(s)
            elif len(s) == i and c > cnt:
                cnt = c
                tmp = [s]
        for i in tmp:
            ans.append(i)

    return sorted(ans)