# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Approach: Modified binary search. 3 cases: mid is equal then return, mid to left is sorted then binary search, mid to right is sorted then binary search
# Complexity: O(log n) time, O(1) space

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return -1
