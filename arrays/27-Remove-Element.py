# Problem: https://leetcode.com/problems/remove-element
# Approach: Use k as a pointer to the next open non-val index in nums, loop through nums inserting non-val digits into nums[k] incrementing k
# Complexity: O(n) time, O(1) space

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
