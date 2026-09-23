# Problem: https://leetcode.com/problems/n-queens/
# Approach: Backtracking using sets to keep track of unavailable diagonals, columns, while rows taken care of by incrementing every time queen is placed.
#           In an n x n board, positive diagnoals will always have the same (r + c) value and negative diagonals will always have the same (r - c) value.
# Complexity: O(n!) time, O(n^2) space
# Enjoyment: 5/5

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []

        used_cols = set()
        used_pos_diags = set()
        used_neg_diags = set()

        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            

            for c in range(n):
                if c in used_cols or r + c in used_pos_diags or r - c in used_neg_diags:
                    continue
                
                board[r][c] = 'Q'
                used_cols.add(c)
                used_pos_diags.add(r + c)
                used_neg_diags.add(r - c)

                backtrack(r + 1)

                board[r][c] = '.'
                used_cols.remove(c)
                used_pos_diags.remove(r + c)
                used_neg_diags.remove(r - c)

        backtrack(0)
        return res
