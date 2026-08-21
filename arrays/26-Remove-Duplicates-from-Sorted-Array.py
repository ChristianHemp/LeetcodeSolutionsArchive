# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approach: Maintain next open index and previous pointers and iterate through nums keeping only non-duplicates, return next_open_index for number of elements k
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_new_index = 0
        prev = None
        
        for num in nums:
            if num == prev:
                continue
            nums[next_new_index] = num
            prev = num
            next_new_index += 1
        
        return next_new_index
