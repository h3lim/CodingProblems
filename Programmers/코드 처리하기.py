def solution(code):
    ret = ""
    mode = 0
    for i in range(len(code)):
        if mode == 0 and i % 2 == 0 and code[i] != "1":
            ret += code[i]
        elif mode == 1 and i % 2 == 1 and code[i] != "1":
            ret += code[i]

        if code[i] == "1" and mode == 0:
            mode = 1
        elif code[i] == "1" and mode == 1:
            mode = 0

    if len(ret) == 0:
        return "EMPTY"

    return ret