# Problem: https://leetcode.com/problems/score-of-a-string/
# Approach: Iterate through string chars stopping 1 before last char and calculating score at each step adding to cumulitive score
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(0, len(s) - 1):
            curr_score = abs(ord(s[i + 1]) - ord(s[i]))

            score += curr_score

        return score
