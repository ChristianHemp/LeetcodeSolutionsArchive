# Problem: https://leetcode.com/problems/counting-bits/
# Approach: Use dp to keep track of previously found number of 1s in bits with same diff (power of 2 offset). Return finished dp array.
# Complexity: O(n) time, O(n) space

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        diff = 1

        for i in range(1, 1 + n):
            if 2 * diff == i:
                diff = i
            dp[i] = dp[i - diff] + 1
        
        return dp
