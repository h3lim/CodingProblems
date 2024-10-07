def solution(n):
    if n == 1:
        return 1
    ans = 0
    left = 1
    curr = 1
    for right in range(2, n + 1):
        curr += right
        if curr == n:
            ans += 1
        while curr > n:
            curr -= left
            left += 1
            if curr == n:
                ans += 1

    return ans
