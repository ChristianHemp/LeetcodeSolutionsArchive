# Problem: https://leetcode.com/problems/isomorphic-strings/
# Approach: Two hashmaps for mapping both sides to check if mapping already exists and if it is correct, returning False at first error
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in s_to_t and s_to_t[c1] != c2) or 
            (c2 in t_to_s and t_to_s[c2] != c1)):
                return False

            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return True
