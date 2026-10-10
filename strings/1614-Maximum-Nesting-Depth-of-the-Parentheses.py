# Problem: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2026-09-28
# Approach: Open parenthesis increment, closed parenthesis decrement, ignore everything else. Keep two counters and return max counter.
# Complexity: O(n) time, O(1) space
# Enjoyment: 4/5

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr_depth = 0

        for c in s:
            if c == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif c == ')':
                curr_depth -= 1
            
        return max_depth
