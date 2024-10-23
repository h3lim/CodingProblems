def solution(my_string):
    ans = 0
    curr = ""
    for i in my_string:
        if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
            if curr != "":
                ans += int(curr)
            curr = ""
        else:
            curr += i

    if curr != "":
        ans += int(curr)
    return ans