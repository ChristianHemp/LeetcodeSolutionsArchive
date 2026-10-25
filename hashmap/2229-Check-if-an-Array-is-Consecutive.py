# Problem: https://leetcode.com/problems/check-if-an-array-is-consecutive/
# Approach: Length of set of nums should be equal to length of nums to check duplicates, largest num - smallest num + 1 should equal length of nums
# Complexity: O(n) time, O(n) space
# Enjoyment: 2/5

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return False
        
        return True if max(nums) - min(nums) + 1 == len(nums) else False
