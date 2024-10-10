import math
def solution(n, words):
    lastAlpha = words[0][-1:]
    s = set()
    s.add(words[0])
    for i in range(1, len(words)):
        if words[i] in s:
            return [(i % n) + 1, math.ceil((i + 1) / n)]
        if lastAlpha != words[i][:1]:
            return [(i % n) + 1, math.ceil((i + 1) / n)]

        s.add(words[i])

        lastAlpha = words[i][-1:]
    return [0, 0]