def solution(bandage, health, attacks):
    time = 0
    currHealth = health
    continousSucceed = 0

    while attacks:
        time += 1

        if time != attacks[0][0]:
            continousSucceed += 1
            if currHealth < health:
                if currHealth + bandage[1] > health:
                    currHealth = health
                else:
                    currHealth += bandage[1]
                if continousSucceed == bandage[0]:
                    if currHealth + bandage[2] > health:
                        currHealth = health
                    else:
                        currHealth += bandage[2]
                    continousSucceed = 0
        else:
            attackTime, damage = attacks.pop(0)
            continousSucceed = 0
            currHealth -= damage

            if currHealth <= 0:
                return -1

    return currHealth