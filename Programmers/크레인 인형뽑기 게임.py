from collections import defaultdict
def solution(board, moves):
    dic = defaultdict(list)
    board = board[::-1]
    stack = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                dic[j].append(board[i][j])

    ans = 0
    for i in moves:
        if len(dic[i - 1]) > 0:
            stack.append(dic[i - 1].pop())

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ans += 1

    return ans * 2