# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Approach: Use a stack that only allows increasing values to calculate all possible rectangles. Iterate through heights getting index and height at each point. Pop from the stack until the current height is less than the height of the top of the stack.
#           Use variable to keep track of where new rectangle starts, which will be the same index we reach after popping. At each pop, calculate whether we have found a new largest rectangle by using height * width, width being (curr index - start index)
#           For remaining values in stack, calculate height for each and replace largest if necessary.
# Complexity: O(n) time, O(n) space
# Enjoyment: 2/5

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        # Use ordered pair to determine length of each rectangle
        for i, height in enumerate(heights):
            rect_start = i  # used to calculate width (index - start)
            # pop all rectangles too large to continue
            while stack and height < stack[-1][1]:
                start_index, curr_height = stack.pop()
                largest = max(largest, curr_height * (i - start_index))
                # new rectangle "starts" at leftmost possible point
                rect_start = start_index
            stack.append((rect_start, height))
        
        # remaining values in stack calculated
        for rect_start, height in stack:
            largest = max(largest, height * (len(heights) - rect_start))
        
        return largest
