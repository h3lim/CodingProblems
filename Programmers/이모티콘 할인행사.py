ans = (0, 0)


def solution(users, emoticons):
    global ans

    def dfs(percent, curr, cnt):
        global ans
        for i in range(len(users)):
            if users[i][0] <= percent:
                curr[i] += (emoticons[cnt] * ((100 - percent) / 100))

        if cnt == len(emoticons) - 1:
            plus, cost = ans
            joinPlus = 0
            for i in range(len(curr)):
                if curr[i] >= users[i][1]:
                    joinPlus += 1
                    curr[i] = 0
            if plus < joinPlus:
                plus = joinPlus
                cost = sum(curr)
            elif plus == joinPlus and sum(curr) > cost:
                cost = sum(curr)
            ans = (plus, int(cost))
            return
        dfs(10, curr.copy(), cnt + 1)
        dfs(20, curr.copy(), cnt + 1)
        dfs(30, curr.copy(), cnt + 1)
        dfs(40, curr.copy(), cnt + 1)

    ans = (0, 0)
    dfs(10, [0] * len(users), 0)
    dfs(20, [0] * len(users), 0)
    dfs(30, [0] * len(users), 0)
    dfs(40, [0] * len(users), 0)
    return ans