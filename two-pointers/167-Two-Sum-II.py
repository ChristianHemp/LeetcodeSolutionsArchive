# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Approach: Maintain left and right pointer, while left index < right index, calcluate current sum and compare to target. If equal, return, if less, increment left by 1, if more, decrement right by 1.
# Complexity: O(n) time, O(1) space
# Enjoyment: 4/5

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
            
