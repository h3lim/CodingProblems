def solution(A, B):
    ans = 0
    if A == B:
        return 0
    for i in range(len(A)):
        ans += 1
        A = A[-1] + A[:-1]
        if A == B:
            return ans
    return -1