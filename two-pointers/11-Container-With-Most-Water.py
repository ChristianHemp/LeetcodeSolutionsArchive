# Problem: https://leetcode.com/problems/container-with-most-water/
# Approach: Keep two pointers, one at start and one at end. At each step calculate area, smaller of two heights times width (right - left)) and update max_area. 
#           Use greedy approach to always keep larger height, increment/decrement other pointer
# Complexity: O(n) time, O(1) space
# Enjoyment: 5/5

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # width = right - left
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
