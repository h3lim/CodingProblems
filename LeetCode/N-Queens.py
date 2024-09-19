from typing import List

class Solution:
    def solveNQueens(n: int) -> List[List[str]]:
        ans = []

        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)

            for c in range(n):
                if c in col or r + c in posDiag or r - c in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return ans


Solution.solveNQueens(4)
