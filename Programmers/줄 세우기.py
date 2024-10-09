import math


def solution(n, k):
    ans = []
    k = k - 1
    numbers = list(range(1, n + 1))

    while n > 0:
        n -= 1
        fact = math.factorial(n)

        index = k // fact

        ans.append(numbers.pop(index))

        k %= fact

    return ans