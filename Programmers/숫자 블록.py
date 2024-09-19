def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
            continue
        max_divisor = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                print(i//j)
                if i // j <= 10000000:
                    max_divisor = max(max_divisor, i // j)
                    break
                max_divisor = max(max_divisor, j)
        result.append(max_divisor)
    return result


solution(10,20)
solution(100,100)
solution(9995,10000)
solution(100000000,100000000)