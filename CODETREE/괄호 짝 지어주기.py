lst = list(input())

stack = []

for i in lst:
    stack.append(i)
    if len(stack) > 1 and stack[-2] == "(" and stack[-1] == ")":
        stack.pop()
        stack.pop()

ans = 0

for i in range(len(stack)):
    if i % 2 == 0 and stack[i] != "(":
        ans += 1
    elif i % 2 == 1 and stack[i] != ")":
        ans += 1

print(ans)