# Problem: https://leetcode.com/problems/house-robber-ii/
# Approach: Dynammic programming, at each index add prev to represent not robbing, or prevprev + nums[i] to represent robbing. Call rob twice excluding first and last house to avoid loop edge case.
# Complexity: O(n) time, O(1) space
# Enjoyment: 4/5

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelper(nums):
            if len(nums) == 1:
                return nums[0]

            dp = [nums[0], max(nums[0], nums[1])]

            for i in range(2, len(nums)):
                temp = dp[1]
                dp[1] = max(dp[1], dp[0] + nums[i]) # 2 choices, dont rob or rob
                dp[0] = temp
        
            return dp[1]
        
        # run rob twice excluding last house then excluding first house, handle edge    case of only 1 house
        return max(robHelper(nums[:-1]), robHelper(nums[1:])) if len(nums) > 1 else nums[0]
