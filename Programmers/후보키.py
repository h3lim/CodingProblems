from itertools import combinations


def solution(relation):
    cand = []
    row = len(relation)
    col = len(relation[0])
    comb = []
    for i in range(1, col + 1):
        comb.extend(combinations(range(col), i))

    for i in comb:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:
            success = True

            for j in cand:
                if set(j).issubset(set(i)):
                    success = False
                    break

            if success == True:
                cand.append(i)

    return len(cand)

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])