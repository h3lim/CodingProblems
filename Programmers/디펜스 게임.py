import heapq
def solution(n, k, enemy):
    hq = []
    hp = n
    i = 0
    while hp >= 0 and i < len(enemy):
        if hp - enemy[i] >= 0:
            hp -= enemy[i]
            heapq.heappush(hq, (-enemy[i], enemy[i]))
        else:
            heapq.heappush(hq, (-enemy[i], enemy[i]))
            hp -= enemy[i]
            if k > 0:
                mx = heapq.heappop(hq)[1]
                hp += mx
                k -= 1
        if hp < 0:
            break
        else:
            i += 1

    return i