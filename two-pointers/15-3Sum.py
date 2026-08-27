# Problem: https://leetcode.com/problems/3sum/
# Approach: Iterate through nums, keeping a j and k pointer. j and k serve a similar role as in 2 sum II, where one starts at the end and one starts at the beginning. while j < k check if the sum is 0, if not increment/decrement accordingly.
#           Duplicates handled through while loop which doesn't allow the same value to be compared again after finding a solution
# Complexity: O(n^2) time, O(n) space
# Enjoyment: 2/5

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        
        return res
