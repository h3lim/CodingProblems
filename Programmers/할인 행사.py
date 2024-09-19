def solution(want, number, discount):
    ans = 0
    dic = dict()
    n = sum(number)
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)):
        tmp = dic.copy()
        if i + n <= len(discount):
            for j in range(i, i + n):
                if discount[j] in want and tmp[discount[j]] > 0:
                    tmp[discount[j]] -= 1
                else:
                    break

            if sum(tmp.values()) == 0:
                ans += 1

    return ans