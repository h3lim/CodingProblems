def solution(order):
    ans = 0
    order = str(order)

    for i in order:
        if i == "3" or i == "6" or i == "9":
            ans += 1

    return ans