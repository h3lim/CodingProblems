from collections import defaultdict
from collections import Counter


def solution(id_list, report, k):
    ans = []
    dic = defaultdict(list)
    reportedUser = defaultdict(int)
    for i in id_list:
        dic[i] = []

    for r in report:
        r1, r2 = r.split()
        if r2 not in dic[r1]:
            dic[r1].append(r2)
            reportedUser[r2] += 1

    suspendedUser = []

    for i, v in reportedUser.items():
        if v >= k:
            suspendedUser.append(i)

    for i, v in dic.items():
        cnt = Counter(v) + Counter(suspendedUser)
        tmp = 0
        for j, n in cnt.items():
            if n == 2:
                tmp += 1

        ans.append(tmp)

    return ans