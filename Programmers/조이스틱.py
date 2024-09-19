def solution(name):
    n = len(name)
    min_move = n - 1  # MAX값

    answer = 0
    for i in range(n):
        # 알파벳 계산
        answer += min(ord(name[i]) - ord('A'), 26 - (ord(name[i]) - ord('A')))

        # 현재 위치에서 다음으로 문자 변경이 필요한 위치를 찾음
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1

        #BBAAAAB

        # i + i: 왼쪽으로 돌아가는 경우
        # n - next: next부터 끝까지 필요한 문자 변경을 위해 오른쪽으로 이동하는 거리
        min_move = min(min_move, i + n - next + min(i, n - next))

    # 총 조작 횟수는 문자 조작 횟수와 커서 이동 횟수를 합산
    answer += min_move

    return answer
