from collections import Counter


def solution(i, j, k):
    ans = 0
    k = str(k)
    for n in range(i, j + 1):
        cnt = Counter(list(str(n)))
        ans += cnt[k]

    return ans
