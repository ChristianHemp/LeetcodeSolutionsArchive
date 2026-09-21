# Problem: https://leetcode.com/problems/palindrome-partitioning/
# Approach: Use backtracking and palindrome checking helper function to check substrings and only append valid substrings to list. If index is equal to the length of the input string, we found a match.
# Complexity: O(n * 2^n) time, O(n) space
# Enjoyment: 4/5

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(index: int, substrings: List[str]) -> None:
            if index == len(s):
                result.append(substrings.copy())
                return
            
            if index >= len(s):
                return
            
            for i in range(index, len(s)):
                if self.is_palindrome(s[index:i + 1]):
                    substrings.append(s[index:i + 1])
                    backtrack(i + 1, substrings)
                    substrings.pop()
        
        backtrack(0, [])
        return result

    
    def is_palindrome(self, string: str) -> bool:
        left, right = 0, len(string) - 1

        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        
        return True
