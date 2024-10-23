def solution(myString, pat):
    for i in range(len(myString), -1, -1):
        if pat == myString[i - len(pat):i]:
            return myString[:i]

    return ""
