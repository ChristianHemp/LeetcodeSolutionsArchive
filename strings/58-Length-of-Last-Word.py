# Problem: https://leetcode.com/problems/length-of-last-word/
# Approach: Strip whitespace from ends of s, split words into list and return length of last element in list
# Complexity: O(n) time, O(n) space

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        words = s.split()

        return len(words[-1])
