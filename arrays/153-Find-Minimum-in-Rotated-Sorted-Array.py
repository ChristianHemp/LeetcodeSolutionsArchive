# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Approach: Use left and right pointers like normal binary search, but check if number before and after mid are greater than or less than respectively. If so, return mid, or mid + 1 respectively. Else continue binary search.
# Complexity: O(log n) time, O(1) space

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[left]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
            
        return min_val
