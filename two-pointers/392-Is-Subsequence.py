# Problem: https://leetcode.com/problems/is-subsequence/
# Approach: Use two pointers to track indicies in strings, iterate through incrementing s index when matching char found
# Complexity: O(n * m) time where n is len of s and m is len of t, O(1) space
# Enjoyment: 3/5

from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, t_index = 0, 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            
            t_index += 1
        
        return True if s_index >= len(s) else False
