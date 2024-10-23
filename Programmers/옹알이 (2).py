def solution(babbling):
    ans = 0
    lst = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        previous = ""
        while True:
            if len(i) == 0:
                break
            if i[:3] in lst and i[:3] != previous:
                previous = i[:3]
                i = i[3:]
            elif i[:2] in lst and i[:2] != previous:
                previous = i[:2]
                i = i[2:]
            else:
                break
        if len(i) == 0:
            ans += 1

    return ans