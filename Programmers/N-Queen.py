def solution(n):

    ans = 0
    col = set()
    posDig = set()
    negDig = set()
    board = [["."] * n for _ in range(n)]

    def backtracking(r):
        nonlocal ans
        if r == n:
            ans += 1
            return

        for c in range(n):
            if c in col or r + c in posDig or r - c in negDig:
                continue

            col.add(c)
            posDig.add(r + c)
            negDig.add(r - c)
            board[r][c] = "Q"
            backtracking(r + 1)
            col.remove(c)
            posDig.remove(r + c)
            negDig.remove(r - c)
            board[r][c] = "."

    backtracking(0)
    return ans
