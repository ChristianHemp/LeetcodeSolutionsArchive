# Problem: https://leetcode.com/problems/max-consecutive-ones/
# Approach: Keep track of consecutive ones using current count, loop through nums checking for 1s updating current count and max count if the current count is greater
# Complexity: O(n) time, O(1) space

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            
            if count > max_count:
                max_count = count
        
        return max_count
