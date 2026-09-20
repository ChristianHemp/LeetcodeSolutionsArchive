# Problem: https://leetcode.com/problems/permutations/
# Approach: Use backtracking and at each recursive call iterate through all numbers in nums, adding and backtracking when an unused num is found. Return when length of curr list is equal to nums.
# Complexity: O(n * n!) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(curr, seen):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)

                    backtrack(curr, seen)

                    curr.pop()
                    seen.remove(num)
        
        backtrack([], set())
        return res
