# Problem: https://leetcode.com/problems/missing-number/
# Approach: Set to keep track of seen numbers, check all numbers in possible range to find missing one
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)

        for i in range(len(nums) + 1):
            if i not in seen:
                return i
