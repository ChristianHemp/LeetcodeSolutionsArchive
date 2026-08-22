# Problem: https://leetcode.com/problems/climbing-stairs/
# Approach: Use dp to keep track of last two values as the ways to climb stairs n is the sum of ways to climb n - 1 and n - 2.
# Complexity: O(n) time, O(1) space

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        dp = [1, 1]

        i = 2
        while i <= n:
            temp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = temp
            i += 1
        return dp[1]
