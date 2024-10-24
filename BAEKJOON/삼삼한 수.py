def is_samsamhan(n):
    if n == 0:
        return "NO"
    s = set()
    lastNum = -1
    while n != 0 and lastNum != 1:
        num = 1
        while num * 3 <= n and num * 3 not in s:
            num *= 3
        n -= num
        s.add(num)
        lastNum = num
    if n == 0:
        return "YES"

    return "NO"
N = int(input())
print(is_samsamhan(N))