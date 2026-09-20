# Problem: https://leetcode.com/problems/subsets-ii/
# Approach: backtracking to build subsets skipping over duplicate starting values
# Complexity: O(n * 2^n) time, O(n) space
# Enjoyment: 4/5

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(index):
            res.append(subset[:])
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return res
