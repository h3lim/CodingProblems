import sys
import math
N = int(sys.stdin.readline())

testCenter = list(map(int, sys.stdin.readline().split()))

B, C = map(int, sys.stdin.readline().split())


def minIndicator(testCenter, ans):
    for i in range(len(testCenter)):
        if testCenter[i] - B <= 0:
            testCenter[i] = 0
        else:
            testCenter[i] -= B
        ans += 1

    if sum(testCenter) == 0:
        return ans

    for i in range(len(testCenter)):
        if testCenter[i] != 0:
            ans += math.ceil(testCenter[i] / C)

    return ans

print(minIndicator(testCenter, 0))


