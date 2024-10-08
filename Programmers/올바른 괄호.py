def solution(s):
    stack = []

    for i in s:
        stack.append(i)

        if len(stack) > 1 and stack[-1] == ")" and stack[-2] == "(":
            stack.pop()
            stack.pop()

    if len(stack) == 0:
        return True

    return False