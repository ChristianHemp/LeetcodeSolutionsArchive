# Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Approach: Make set of all possible values, discard values when found and return remaining values
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        possible = set(range(1, len(nums) + 1))
        res = []

        for num in nums:
            possible.discard(num)
        
        return list(possible)
