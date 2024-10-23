def solution(chicken):
    ans = 0

    while chicken > 9:
        val = chicken // 10
        tmp = chicken % 10
        ans += val
        chicken = val + tmp

    return ans