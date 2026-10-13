# Problem: https://leetcode.com/problems/maximum-alternating-sum-of-squares/?envType=daily-question&envId=2026-10-13
# Approach: Square numbers to get final values, then sort taking negative of first half and positives of second half to get optimal greedy choices
# Complexity: O(n log n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            nums[i] *= nums[i]
        
        nums.sort()

        return -sum(nums[:length // 2]) + sum(nums[length // 2:])
