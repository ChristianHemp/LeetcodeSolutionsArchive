# Problem: https://leetcode.com/problems/sum-of-squares-of-special-elements/?envType=daily-question&envId=2026-10-11
# Approach: Simple iteration keeping sum value
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(len(nums)):
            if (n / (i + 1)).is_integer():
                res += nums[i] * nums[i]
        
        return res
