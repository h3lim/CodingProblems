from collections import deque
def solution(bridge_length, weight, truck_weights):
    ans = 0
    currWeight = 0
    dq = deque(truck_weights)
    passingTruck = deque([0] * bridge_length)

    while dq:
        ans += 1

        currWeight -= passingTruck.popleft()

        if currWeight + dq[0] <= weight:
            currWeight += dq[0]
            passingTruck.append(dq.popleft())
        else:
            passingTruck.append(0)

    ans = ans + bridge_length

    return ans

solution(2,10,[7,4,5,6])