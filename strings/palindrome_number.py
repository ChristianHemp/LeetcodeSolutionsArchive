# Problem: https://leetcode.com/problems/palindrome-number/
# Approach: Turn integer into string then reverse the string and check equality
# Complexity: O(n) time, O(n) space

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
