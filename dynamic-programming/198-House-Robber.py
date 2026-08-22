# Problem: https://leetcode.com/problems/house-robber/
# Approach: Use dp array to keep track of max amount of money to have made at that index. For each iteration while i < length of array, set dp[i] to the sum of nums[i] to dp[i - 2].
#           This is the default case where we choose to rob the current house available. The second case is to not rob the house, however, to account for double skips (ie: 2, 1, 1, 2),
#           if dp[i - 2] is greater than dp[i - 1], move the value over one so that dp[i - 1] still accurately reflects max amount possible at that time having not robbed the current house.
# Complexity: O(n) time, O(n) space
# Enjoyment: 5/5

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]
        elif length <= 2:
            return max(nums[0], nums[1])
        
        # initialize dp array
        dp = [0] * length
        dp[0], dp[1] = nums[0], nums[1]

        i = 2
        # 2 choices: 1 - rob house, 2 - skip house
        while i < length:
            # default case 1
            dp[i] = dp[i - 2] + nums[i]
            
            # maintains order for choice 2 (dp[i-1] must be max possible money gained having not robbed previous house)
            if dp[i - 2] > dp[i - 1]:
                dp[i - 1] = dp[i - 2]
    
            i += 1

        return max(dp[-1], dp[-2])
