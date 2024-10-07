def solution(lottos, win_nums):
    lottoRank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    mn = 0
    zeroNum = 0
    for i in lottos:
        if i in win_nums:
            mn += 1
        elif i == 0:
            zeroNum += 1

    return [lottoRank[mn + zeroNum], lottoRank[mn]]


