def solution(number, k):
    ans = []
    length = len(number) - k

    for i, v in enumerate(number):
        while len(ans) >= 1 and ans[-1] < int(v) and k != 0:
            k -= 1
            ans.pop()
        ans.append(int(v))
    ans = str(ans)
    return "".join(ans)
print(solution("4177252891",4))