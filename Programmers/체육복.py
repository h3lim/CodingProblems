def solution(n, lost, reserve):
    actual_lost = [l for l in lost if l not in reserve]
    actual_reserve = [r for r in reserve if r not in lost]

    actual_lost.sort()
    actual_reserve.sort()

    participation = n - len(actual_lost)

    for i in actual_lost:
        if i - 1 in actual_reserve:
            participation += 1
            actual_reserve.remove(i - 1)
        elif i + 1 in actual_reserve:
            participation += 1
            actual_reserve.remove(i + 1)

    return participation