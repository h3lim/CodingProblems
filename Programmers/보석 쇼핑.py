from collections import defaultdict


def solution(gems):
    ans = [0, len(gems)]
    dic = defaultdict(int)
    jewels = len(set(gems))
    left = 0
    contained_jewels = 0

    for right in range(len(gems)):
        dic[gems[right]] += 1
        if dic[gems[right]] == 1:
            contained_jewels += 1

        while jewels == contained_jewels:
            if right - left < ans[1] - ans[0]:
                ans[0], ans[1] = left + 1, right + 1

            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                contained_jewels -= 1
            left += 1

    return ans



