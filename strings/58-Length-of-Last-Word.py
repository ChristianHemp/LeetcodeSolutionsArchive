# Problem: https://leetcode.com/problems/length-of-last-word/
# Approach: Strip whitespace from ends of s, iterate from back until whitespace found
# Complexity: O(n) time, O(1) space

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        length = len(string) - 1
        i = length

        while i >= 0:
            if string[i] == ' ':
                return length - i
            else:
                i -= 1
        
        return len(string)
