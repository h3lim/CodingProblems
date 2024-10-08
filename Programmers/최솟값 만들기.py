def solution(A, B):
    ans1 = 0
    ans2 = 0

    straightA, reversedA = sorted(A), sorted(A, reverse=True)
    straightB, reversedB = sorted(B), sorted(B, reverse=True)

    for i in range(len(straightA)):
        ans1 += straightA[i] * reversedB[i]
    for i in range(len(straightA)):
        ans2 += straightB[i] * reversedA[i]

    return min(ans1, ans2)


