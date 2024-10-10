import math
def solution(n):
    ans = 0
    for i in range(2, n + 1):
        tmp = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                if j * j == i:
                    tmp += 1
                else:
                    tmp += 2
            if tmp >= 3:
                break

        if tmp == 2:
            ans += 1

    return ans