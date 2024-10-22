def solution(quiz):
    ans = []
    for i in quiz:
        curr = ""
        tmpAns = 0
        flag = 0
        for j, val in enumerate(i):
            if val != "=" and flag == 0:
                curr += val
            elif val == "=":
                flag = 1
            if flag == 1:
                break
        tmpAns = int(i[j + 2:])
        if eval(curr) == tmpAns:
            ans.append("O")
        else:
            ans.append("X")

    return ans