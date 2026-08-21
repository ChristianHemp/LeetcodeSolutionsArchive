# Problem: https://leetcode.com/problems/flood-fill/
# Approach: Recursive dfs graph-matrix-like traversal changing all adjacent indices of original color to flood fill. Base cases for out of bounds and not bein original color.
# Complexity: O(n * m) time, O(n * m) space


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image
        
        def dfs(r: int, c: int) -> None:
            # base case out of matrix bounds
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return

            # base case different color from original
            if image[r][c] != original_color:
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
