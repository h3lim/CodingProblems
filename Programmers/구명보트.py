from collections import deque


def solution(people, limit):
    ans = 0
    people.sort()
    dq = deque()

    for i in people:
        dq.append(i)

    while dq:
        heaviestPerson = dq.pop()
        if dq and heaviestPerson + dq[0] <= limit:
            dq.popleft()
        ans += 1

    return ans


solution([80, 40, 50, 85],100)