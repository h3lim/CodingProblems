def solution(s):
    if len(s) < 2:
        return 1

    ans = 0

    def check_palindrome(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        odd = check_palindrome(i, i)
        even = check_palindrome(i, i + 1)
        currMax = max(odd, even)
        ans = max(ans, currMax)

    return ans