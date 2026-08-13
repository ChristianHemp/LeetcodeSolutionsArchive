# Problem: https://leetcode.com/problems/concatenation-of-array/
# Approach: Create array twice the length of nums (n), loop through nums copying indicies i from i and i + n from i.
# Complexity: O(n) time, O(n) space

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans
