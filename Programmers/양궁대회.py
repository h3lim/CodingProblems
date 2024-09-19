def solution(n, info):
    def whoWin(curr,info):
        l, a = 0, 0
        for i in range(len(curr)):
            if curr[i] > info[i]:
                l += (11 - i - 1)
            elif curr[i] <= info[i] and info[i] != 0:
                a += (11 - i - 1)

        print(l,a)

        if l > a:
            return l - a
        return 0

    def dfs(curr, k, i):
        nonlocal mx, ans
        flag = 0
        if k == 0 or i == len(curr)-1:
            print(curr, k, i, mx, ans)
            diff = whoWin(curr,info);
            if diff > 0:
                if k != 0:
                    curr[10] = k
                    flag = 1
                if diff > mx:
                    mx = diff
                    ans = curr[:]
                elif diff == mx:
                    lastelmt1, lastelmt2 = 0, 0
                    for i in range(len(curr)):
                        if ans[i] > 0:
                            lastelmt1 = i
                        if curr[i] > 0:
                            lastelmt2 = i
                    if lastelmt2 > lastelmt1:
                        ans = curr[:]

                if flag == 1:
                    curr[10] = 0
            return

        if k > info[i]:
            curr[i] = info[i] + 1
            dfs(curr, k - (info[i]+1), i + 1)
            curr[i] = 0
            dfs(curr,k,i+1)
        else:
            dfs(curr, k, i + 1)
    ans = [-1]
    curr = [0] * 11
    mx = 0

    dfs(curr, n,0)
    print(ans)
solution(3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1] )

