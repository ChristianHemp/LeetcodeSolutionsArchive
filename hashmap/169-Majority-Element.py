# Problem: https://leetcode.com/problems/majority-element/
# Approach: Use hashmap to track counts, return when counts exceeds n
# Complexity: O(n) time, O(n) space

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums) / 2

        for num in nums:
            counts[num] += 1
            if counts[num] > n:
                return num
