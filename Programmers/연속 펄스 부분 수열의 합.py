def solution(sequence):
    def kadane(lst):
        max_current = max_global = lst[0]

        for i in range(1, len(lst)):
            max_current = max(lst[i], max_current + lst[i])

            if max_current > max_global:
                max_global = max_current

        return max_global

    negativeFirst = sequence.copy()
    positiveFirst = sequence.copy()

    n = -1
    for i in range(len(negativeFirst)):
        negativeFirst[i] *= n
        n *= -1

    n = 1

    for i in range(len(positiveFirst)):
        positiveFirst[i] *= n
        n *= -1

    ans = max(kadane(negativeFirst), kadane(positiveFirst))

    return ans