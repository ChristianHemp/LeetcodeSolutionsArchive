# Problem: https://leetcode.com/problems/subsets/
# Approach: Use a recursive decision tree to account for all possibilities of included and excluded values in nums. Correct order adds the actual list as a subset first, then gradually moves towards appending empty set
# Complexity: O(2^n) time, O(n) space

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
