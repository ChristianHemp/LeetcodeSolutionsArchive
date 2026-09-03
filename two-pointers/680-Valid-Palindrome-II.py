# Problem: https://leetcode.com/problems/valid-palindrome-ii/
# Approach: Use two pointers, when first mistake reached, call helper palindrome check on both possible deletes, returning that result. 
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
        
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    is_palindrome(s[left+1:right+1]) or
                    is_palindrome(s[left:right])
                    )

            left += 1
            right -= 1
        
        return True
