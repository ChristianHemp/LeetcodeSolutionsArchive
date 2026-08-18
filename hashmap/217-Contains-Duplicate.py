# Problem: https://leetcode.com/problems/contains-duplicate/
# Approach: Maintain hashmap of seen nums, if duplicate key found return tree, else return false
# Complexity: O(n) time, O(n) space

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = num
        return False
