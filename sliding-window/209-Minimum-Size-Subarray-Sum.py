# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/
# Approach: Use sliding window, if sum of values in current window greater than target, update min_length, decrement current total, and increment left pointer
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        total = 0
        min_len = float('inf')

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                min_len = min(min_len, R - L + 1)
                total -= nums[L]
                L += 1
        
        return 0 if min_len == float('inf') else min_len
