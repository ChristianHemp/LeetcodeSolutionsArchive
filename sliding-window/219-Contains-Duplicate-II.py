# Problem: https://leetcode.com/problems/contains-duplicate-ii/
# Approach: Use sliding window with set to check for duplicates in range k
# Complexity: O(n) time, O(k) space where k is max size of window
# Enjoyment: 3/5

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
        
        return False
