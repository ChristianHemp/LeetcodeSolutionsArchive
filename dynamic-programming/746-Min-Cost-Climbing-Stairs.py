# Problem: https://leetcode.com/problems/min-cost-climbing-stairs/
# Approach: Use dp array of 2 indices adding the cost at each step to the lower of the two indices. Also included approach with full dp array, in which case add to lower of previous two indices
# Complexity: O(n) time, O(1) space
# Enjoyment: 4/5

class Solution:
    # Use only 2 indices
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Initialize dp array
        dp = [cost[0], cost[1]]

        i = 2
        while i < len(cost):
            temp = dp[1]
            # Next lowest step cost is cost + minimum of previous 2 steps
            dp[1] = min(dp[0], dp[1]) + cost[i]
            dp[0] = temp

            i += 1
        
        return min(dp[0], dp[1])
    
    """
    # Use full DP array
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp array tracks least cost to reach i level on stair
        dp = [0] * len(cost)

        # steps 0 and 1 have set total cost
        dp[0], dp[1] = cost[0], cost[1]

        i = 2
        while i < len(cost):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
            i += 1
        
        return min(dp[-1], dp[-2])
    """
