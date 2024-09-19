import math
def solution(r1, r2):
    ans = 0
    for i in range(1, r2 + 1):
        y2 = math.sqrt(r2 ** 2 - i ** 2)

        if r1 ** 2 - i ** 2 < 0:
            y1 = 0
        else:
            y1 = math.sqrt(r1 ** 2 - i ** 2)

        ans += math.floor(y2) - math.ceil(y1) + 1

    return ans * 4