# Problem: https://leetcode.com/problems/product-of-array-except-self/
# Approach: Maintain a prefix and suffix array which, at each index, contains the product of all values up to, but excluding that index, for the prefix and the suffix contains the product of al values from the end to that index, excluding that index
#           Return resulting array which contains the product of the prefix and suffix arrays at each index
# Complexity: O(n) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        res = []
        
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suf[i] = 1
            else:
                suf[i] = nums[i + 1] * suf[i + 1]
        
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])
            
        return res
