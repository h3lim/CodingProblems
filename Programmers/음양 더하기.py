def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            ans += -(absolutes[i])
        else:
            ans += absolutes[i]

    return ans