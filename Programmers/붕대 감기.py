def solution(bandage, health, attacks):
    fullStn = health
    attackTime = 0
    cont = 0
    for i in range(attacks[len(attacks) - 1][0] + 1):
        if i == attacks[attackTime][0]:
            health -= attacks[attackTime][1]
            cont = 0
            attackTime += 1
            if health < 1:
                return - 1
        else:
            cont += 1
            if cont == bandage[0]:
                health = health + (bandage[1] + bandage[2])
                cont = 0
            else:
                health = health + bandage[1]

            if health > fullStn:
                health = fullStn
    return health