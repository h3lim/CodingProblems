from collections import deque


def solution(queue1, queue2):
    ans = 0

    sum1, sum2 = sum(queue1), sum(queue2)
    q = sorted(queue1 + queue2)
    s = sum1 + sum2
    goal = s // 2
    left = curr = success = 0

    queue1, queue2 = deque(queue1), deque(queue2)

    for i in range(len(queue1) * 3):
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return ans
        ans += 1

    return -1