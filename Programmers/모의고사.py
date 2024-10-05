def solution(answers):
    ans = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    tmp = [0, 0, 0]

    for i, a in enumerate(answers):
        if student1[i % len(student1)] == a:
            tmp[0] += 1
        if student2[i % len(student2)] == a:
            tmp[1] += 1
        if student3[i % len(student3)] == a:
            tmp[2] += 1

    mx = max(tmp)

    for idx, i in enumerate(tmp):
        if mx == i:
            ans.append(idx + 1)
    return ans