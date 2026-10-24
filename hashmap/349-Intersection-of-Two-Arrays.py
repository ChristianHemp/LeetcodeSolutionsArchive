# Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Approach: Hashset to track numbers in one list, check for matches in other list
# Complexity: O(n + m) time, O(n) space
# Enjoyment: 3/5

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        result = set()

        for num in nums2:
            if num in seen:
                result.add(num)

        return list(result)
