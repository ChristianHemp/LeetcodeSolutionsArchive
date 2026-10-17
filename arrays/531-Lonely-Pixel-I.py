# Problem: https://leetcode.com/problems/lonely-pixel-i/
# Approach: hashmap keeps track of number of black spaces in each row and column, traverse matrix twice first filling hashmap then looking for lonely black squares
# Complexity: O(n * m) time, O(n + m) space
# Enjoyment: 3/5

from collections import defaultdict

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        result = 0

        row_counts = defaultdict(int)
        col_counts = defaultdict(int)

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    if row_counts[i] == 1 and col_counts[j] == 1:
                        result += 1
        
        return result
