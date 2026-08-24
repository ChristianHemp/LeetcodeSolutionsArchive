# Problem: https://leetcode.com/problems/valid-palindrome/
# Approach: Maintain left and right pointer iterating closer to middle at each loop. Two while loops allow for extra iterations if current pointer is pointing at non-alphanumeric value in s.
# Complexity: O(n) time, O(1) space
# Enjoyment: 2/5

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        left = 0
        right = len(s) - 1

        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
