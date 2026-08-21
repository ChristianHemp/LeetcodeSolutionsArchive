# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Approach: Loop through haystack up until index + length of the needle (plus one for edge case haystack == needle), check slice from haystack indicies i to i + length of needle and return starting index
# Complexity: O(n * m) time, O(1) space

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        
        return -1
