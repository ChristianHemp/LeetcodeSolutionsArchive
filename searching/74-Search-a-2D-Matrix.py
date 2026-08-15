# Problem: https://leetcode.com/problems/search-a-2d-matrix/
# Approach: Perform a modified binary search to identify correct row, then binary search row when found for target
# Complexity: O(log(n) + log(m)) time where n is num of rows and m is num of columns, O(1) space

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = None

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break

            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][0]:
                left = mid + 1

        if row is None:
            return False

        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        
        return False
