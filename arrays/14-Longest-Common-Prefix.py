# Problem: https://leetcode.com/problems/longest-common-prefix/
# Approach: Only look at smallest and largest strings, compare each character adding to lcp until no longer equivalent, then return.
# Complexity: O(n) time, O(1) space

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
