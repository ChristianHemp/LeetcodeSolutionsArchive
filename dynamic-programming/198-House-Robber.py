# Problem: https://leetcode.com/problems/house-robber/
# Approach: Use dp array to keep track of max amount of money to have made at that index. At each new house we can choose to rob or skip, and dp[i] will keep the larger of the two values.
# Complexity: O(n) time, O(n) space (could optimize to O(1) space using two pointers, but dp logic clearer this way)
# Enjoyment: 5/5

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]
        elif length <= 2:
            return max(nums[0], nums[1])
        
        dp = [0] * length
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        i = 2
        while i < length:
            # choice 1: rob house i
            # choice 2: skip house i
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

            i += 1

        return dp[-1]
