# Problem: https://leetcode.com/problems/plus-one/
# Approach: Nested for loop to brute force the solution
# Complexity: O(n²) time, O(1) space
# Note: Inteded to be solved with hash map, completed in first few hours of learning programming so solved brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for x in range(n):
            for y in range(x + 1, n):
                if nums[x] + nums[y] == target:
                    return[x, y]
