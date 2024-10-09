def solution(skill, skill_trees):
    ans = 0
    s = set(skill)
    tree = []
    for i in skill_trees:
        for j in range(65, 91):
            if chr(j) not in s:
                i = i.replace(chr(j), "")
        tree.append(i)

    for i in tree:
        length = min(len(skill), len(i))

        if skill[:length] == i[:length]:
            ans += 1

    return ans