def can_complete_puzzles(diffs, times, limit, mid):
    total_time = 0
    for i in range(len(diffs)):
        if i == 0:
            prev_time = 0
        else:
            prev_time = times[i - 1]

        if diffs[i] <= mid:
            total_time += times[i]
        else:
            mistake = diffs[i] - mid
            total_time += (times[i] + prev_time) * mistake + times[i]
    if total_time <= limit:
        return True

    return False


def solution(diffs, times, limit):
    left, right = 1, 100000

    while left < right:
        mid = left + (right - left) // 2

        if can_complete_puzzles(diffs, times, limit, mid):
            right = mid
        else:
            left = mid + 1

    return left