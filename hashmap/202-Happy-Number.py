# Problem: https://leetcode.com/problems/happy-number/
# Approach: Keep a set of seen numbers and parse int into string to do ** 2 for each char, return true if the result is 1, else add to set. If already seen, return false.
# Complexity: O(log n) time, O(log n) space
# Enjoyment: 3/5

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            numStr = str(n)
            n = 0
            for d in numStr:
                n += (int(d) ** 2)
            if n == 1:
                return True
        return False
