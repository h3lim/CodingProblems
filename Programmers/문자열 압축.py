def solution(s):
    ans = len(s)
    cnt = 1
    for i in range(1,(len(s)//2)+1):
        res = ""
        base = s[:i]
        for j in range(i,len(s)+1, i):
            endIdx = min(j+i,len(s))
            if base == s[j:endIdx]:
                cnt += 1
            else:
                if cnt >= 2:
                    res += str(cnt)

                res += base
                base = s[j:endIdx]
                cnt = 1
        res += base
        ans = min(ans, len(res))
    return ans