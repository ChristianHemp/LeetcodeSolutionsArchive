# Problem: https://leetcode.com/problems/unique-paths-ii/
# Approach: Built upon submission for LC 62 (see /dynamic-programming/62-Unique-Paths.py). Changes: Instead of always having last index in each row be 1, it mirrors value seen in the last index of previous row.
#           This helps cover cases where there is a rock somewhere in the last column. Additionally, curr_row is only updated with the sum of right and down if it isn't a rock in the given grid, otherwise it is set to 0, as there are no paths from there to the end.
# Complexity: O(r * c) time, O(c) space where r is num of rows and c is num of cols
# Enjoyment: 4/5

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        prev_row = [0] * cols
        prev_row[-1] = 1
        
        for r in range(rows - 1, -1, -1):
            curr_row = [0] * cols

            if obstacleGrid[r][-1] == 1:
                curr_row[-1] = 0
            else:
                curr_row[-1] = prev_row[-1]

            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0
                else:
                    curr_row[c] = prev_row[c] + curr_row[c + 1]
            
            prev_row = curr_row
        
        return curr_row[0]
