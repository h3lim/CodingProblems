T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    build = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        mn = float("inf")
        if build[i-2] < build[i] and build[i-1] < build[i] and build[i+1] < build[i] and build[i+2] < build[i]:
            mn = min(min(build[i]- build[i-2], build[i] - build[i-1]),min(build[i]- build[i+2], build[i] - build[i+1]))
        if mn != float("inf"):
            ans += mn

    print("#{} {}".format(test_case, ans))