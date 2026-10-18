# Problem: https://leetcode.com/problems/largest-number/
# Approach: Use custom compare method to sort strings based on largest possible ordering. Cast to int then back to str to remove extra 0s
# Complexity: O(n log n) time, O(n) space
# Enjoyment: 2/5

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i, num in enumerate(nums):
            nums[i] = str(num)
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int(''.join(nums)))
