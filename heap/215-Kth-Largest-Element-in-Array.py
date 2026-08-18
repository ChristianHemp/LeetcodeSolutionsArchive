# Problem: https://leetcode.com/problems/k-closest-points-to-origin/
# Approach: Use a min heap and pop values till size k, then return the 0th index which will be the kth largest. (Alternatively use quickselect for O(n) average time)
# Complexity: O(n log k) time where n is the size of nums and k is the passed k value, O(1) space

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]
