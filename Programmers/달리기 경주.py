from collections import defaultdict


def solution(players, callings):
    dic = defaultdict(int)

    for i in range(len(players)):
        dic[players[i]] = i

    for i in callings:
        tmp = players[dic[i] - 1]
        players[dic[i] - 1] = i
        players[dic[i]] = tmp

        dic[tmp] += 1
        dic[i] -= 1

    return players
