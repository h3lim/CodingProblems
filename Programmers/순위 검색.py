from collections import defaultdict
from itertools import combinations


def solution(info, query):
    ans = list()
    dic = defaultdict(list)
    for w in info:
        word = w.split()
        score = int(word[-1])
        word = word[:-1]

        for i in range(5):
            c = list(combinations(range(4), i))
            for j in c:
                tmp = word.copy()
                for k in j:
                    tmp[k] = "-"
                key = "".join(tmp)
                dic[key].append(score)

    for v in dic.values():
        v.sort()

    for q in query:
        target = int(q.split()[-1])
        word = "".join(q.replace(" and", "").split()[:-1])
        scoreList = dic[word]

        if not scoreList:
            ans.append(0)
            continue
        l, r = 0, len(scoreList)
        while l < r:
            mid = l + (r - l) // 2
            if scoreList[mid] < target:
                l = mid + 1
            else:
                r = mid
        ans.append(len(scoreList) - l)
    return ans





solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 500","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])