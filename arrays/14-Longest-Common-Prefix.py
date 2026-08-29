# Problem: https://leetcode.com/problems/longest-common-prefix/
# Approach: Only look at smallest and largest strings, compare each character adding to chars then return the join of chars
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        longest = max(strs)
        shortest = min(strs)
        chars = []

        for i in range(len(shortest)):
            if shortest[i] == longest[i]:
                chars.append(shortest[i])
            else:
                break
        
        return ''.join(chars)
