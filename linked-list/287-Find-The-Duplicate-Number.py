# Problem: https://leetcode.com/problems/find-the-duplicate-number/
# Approach: Floyd's cycle detection algorithm to find intersection in cycle. Distance from the intersection of fast and slow pointers to the beginning of cycle (where the duplicate is)
#           is always equal to the distance (in terms of number of nodes) from the start to the beginning. Use two pointers and return the intersection.
# Complexity: O(n) time, O(1) space
# Enjoyment: 1/5

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Distance from start to beginning of cycle is always equal to distance of intersection of fast and slow to the beginning of cycle, start new pointer and increment both till intersection
        new_slow = 0
        while True:
            slow = nums[slow]
            new_slow = nums[new_slow]
            if new_slow == slow:
                return slow
