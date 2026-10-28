# Problem: https://leetcode.com/problems/jump-game/
# Approach: Start from end, maintain goal variable that tracks the required jump value to get to next index
# Complexity: O(n) time, O(1) space
# Enjoyment: 3/5

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
