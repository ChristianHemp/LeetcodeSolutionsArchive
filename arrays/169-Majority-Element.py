# Problem: https://leetcode.com/problems/majority-element/
# Approach: Increment count if same num is found as candidate, if 0 replace candidate, otherwise decrement candidate.
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
