# Problem: https://leetcode.com/problems/reverse-string/
# Approach: Two pointers at start and end truncating towards middle, swap chars at each point
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
