# Problem: https://leetcode.com/problems/merge-sorted-array/
# Approach: Maintain 3 pointers for last indices of both lists and the last non-placeholder index for nums1. Compare values from largest to smallest and sort.
# Complexity: O(n) time, O(1) space

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1   # last index in nums1
        i = n - 1   # last index in nums 2
        j = m - 1   # last non-placeholder index in nums 1

        while i >= 0 and j >= 0:
            if nums2[i] > nums1[j]:
                nums1[k] = nums2[i]
                i -= 1
            else:
                nums1[k] = nums1[j]
                j -= 1
            k -= 1
        
        if i >= 0:
            while i >= 0:
                nums1[k] = nums2[i]
                i -= 1
                k -= 1
        else:
            while j >= 0:
                nums1[k] = nums1[j]
                j -= 1
                k -= 1
