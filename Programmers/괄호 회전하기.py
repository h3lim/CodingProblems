def solution(s):
    ans = 0
    for i in range(len(s)):
        str1 = str(s[i:len(s)] + s[:i])
        check = 1
        while check != 0:
            check = 0
            if "[]" in str1:
                tmp = list(str1)
                del tmp[str1.index("[]")]
                del tmp[str1.index("[]")]
                str1 = "".join(tmp)
                check = 1
            if "()" in str1:
                tmp = list(str1)
                del tmp[str1.index("()")]
                del tmp[str1.index("()")]
                str1 = "".join(tmp)
                check = 1
            if "{}" in str1:
                tmp = list(str1)
                del tmp[str1.index("{}")]
                del tmp[str1.index("{}")]
                str1 = "".join(tmp)
                check = 1
        if len(str1) == 0:
            ans += 1
    return ans