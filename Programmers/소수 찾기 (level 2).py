def solution(numbers):
    lst = []
    visited = [False] * (len(numbers))

    def permutation(curr):
        if 1 <= len(curr) <= len(numbers):
            lst.append(int("".join(curr)))
            if len(curr) == len(numbers):
                return

        for i in range(len(numbers)):
            if visited[i] == True:
                continue
            visited[i] = True
            permutation(curr + [numbers[i]])
            visited[i] = False

    permutation([])

    lst = list(set(lst))
    ans = 0
    print(lst)
    for i in lst:
        tmp = 0
        for k in range(1, i):
            if i % k == 0:
                if k * k == i:
                    tmp += 1
                else:
                    tmp += 2
            if tmp >= 3:
                break
        if tmp == 2:
            ans += 1
    return ans

