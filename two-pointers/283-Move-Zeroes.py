# Problem: https://leetcode.com/problems/move-zeroes/
# Approach: two pointers, left increments every time nonzero found, when nonzero found swap with leftmost zero
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
