def solution(storey):
    ans = 0

    while storey != 0:
        remainder = storey % 10

        if remainder > 5:
            ans += 10 - remainder
            storey += 10

        elif remainder < 5:
            ans += remainder

        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            ans += remainder

        storey //= 10

    return ans