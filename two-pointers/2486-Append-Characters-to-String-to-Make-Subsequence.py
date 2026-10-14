# Problem: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
# Approach: Two pointers increment t pointers when new matching character found return length of t minus the number of matching characters found to get amount needed to form subsequence
# Complexity: O(n + m) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) - j
