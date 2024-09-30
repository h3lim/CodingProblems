def solution(n, times):
    left = 1
    right = max(times) * n  # 최대 시간 설정
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 중간 시간 계산
        total = 0

        for time in times:
            total += mid // time  # 각 심사관이 처리할 수 있는 사람 수 합계

        if total >= n:
            answer = mid
            right = mid - 1  # 시간을 줄여서 더 작은 값 탐색
        else:
            left = mid + 1  # 시간을 늘려서 더 큰 값 탐색

    return answer


print(solution(6,[7,10]))