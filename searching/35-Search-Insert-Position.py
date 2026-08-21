# Problem: https://leetcode.com/problems/search-insert-position/
# Approach: Binary search through array for target value, if not found, last value of mid will be retained. if target value greater than current mid value, expected index is mid + 1, otherwise its mid
# Complexity: O(log n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        # mid value retained from last loop iteration
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
