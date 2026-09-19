# Problem: https://leetcode.com/problems/generate-parentheses/
# Approach: Backtracking, try to add new open parenthesis or closed parenthesis. If more closed than open return or return if more open parenthesis than n
# Complexity: O(4^n/sqrt(n)), O(n) space
# Enjoyment: 3/5

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(num_open, num_closed, curr_chars):
            # invalid string
            if num_open < num_closed or num_open > n:
                return
            
            # valid string found
            if len(curr_chars) == 2 * n:
                res.append(''.join(curr_chars))
                return
            
            # add new open bracket
            curr_chars.append('(')
            backtrack(num_open + 1, num_closed, curr_chars)
            curr_chars.pop()

            # add new closed bracket
            curr_chars.append(')')
            backtrack(num_open, num_closed + 1, curr_chars)
            curr_chars.pop()
        
        backtrack(0, 0, [])
        return res
