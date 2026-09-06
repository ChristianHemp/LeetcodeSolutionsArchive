# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Approach: Use sliding window while right pointer is greater than left pointer calculating profit at each step. If right is larger, update left to be right.
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] <= prices[left]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
        
        return max_profit
