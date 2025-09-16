# Problem: https://leetcode.com/problems/longest-common-prefix/
# Approach: Find max and min within the list of strings (lexographically) loop through the indexes checking for equality
# Complexity: O(n*m) time, O(1) space

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        largest = max(strs)
        smallest = min(strs)
        if len(strs) == 0:
            return lcp
        for i in range(len(smallest)):
            if smallest[i] == largest[i]:
                lcp += smallest[i]
            else:
                break

        return lcp
