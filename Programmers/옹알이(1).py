def solution(babbling):
    ans = 0
    s = set({"aya", "ye", "woo", "ma"})

    for i in babbling:
        idx = 0
        while True:
            if idx < len(i) and i[idx:idx + 2] in s:
                idx += 2
            elif idx < len(i) and i[idx:idx + 3] in s:
                idx += 3
            else:
                break

        if idx == len(i):
            ans += 1

    return ans