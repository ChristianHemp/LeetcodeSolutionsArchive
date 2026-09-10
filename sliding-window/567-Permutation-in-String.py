# Problem: https://leetcode.com/problems/permutation-in-string/
# Approach: Use two dictionaries mapping chars to counts for current window and target. Use fixed size sliding window and count matching chars as window moves. If matching chars = length of s1, return True
# Complexity: O(n + m) time, O(n + m) space where n is size of s1 and m is size of s2
# Enjoyment: 3/5

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = defaultdict(int)   # char counts for target
        window = defaultdict(int)   # char counts for curr window

        for c in s1:
            target[c] += 1
        
        L = 0
        matching_chars = 0

        # fixed size sliding window
        for R in range(len(s2)):
            window[s2[R]] += 1

            if s2[R] in target and window[s2[R]] <= target[s2[R]]:
                matching_chars += 1 # char at R matches a target char

            if R - L + 1 > len(s1):
                if s2[L] in target and window[s2[L]] <= target[s2[L]]:
                    matching_chars -= 1 # char at L out of curr window
                
                window[s2[L]] -= 1
                L += 1
            
            # all chars match
            if matching_chars == len(s1):
                return True

        return False
        
