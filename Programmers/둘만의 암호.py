def solution(s, skip, index):
    ans = ""
    for i in range(len(s)):
        cnt = index
        tmp = ord(s[i])
        while cnt > 0:
            if tmp + 1 > 122:
                tmp = 97
                if chr(tmp) in skip:
                    continue
                else:
                    cnt -= 1
            else:
                tmp = tmp + 1
                if chr(tmp) in skip:
                    continue
                else:
                    cnt -= 1
        ans += chr(tmp)

    return ans
