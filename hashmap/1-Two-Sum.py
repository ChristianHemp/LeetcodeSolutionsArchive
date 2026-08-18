# Problem: https://leetcode.com/problems/two-sum/
# Approach: Iterate through nums and maintain hashmap with values of nums as the keys and indicies as the values. Calculate complements (target - curr) and see if in hashmap
# Complexity: O(n) time, O(n) space

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            else:
                hash_map[nums[i]] = i
  
