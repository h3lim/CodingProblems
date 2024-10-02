def solution(sequence, k):
    left = 0
    curr = sequence[0]
    ans = [0, len(sequence)]
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]

    for right in range(1, len(sequence)):
        curr += sequence[right]
        if curr == k:
            if ans[1] - ans[0] > right - left:
                ans[0], ans[1] = left, right

        while curr > k:
            curr -= sequence[left]
            left += 1
            if curr == k:
                if ans[1] - ans[0] > right - left:
                    ans[0], ans[1] = left, right

    return ans