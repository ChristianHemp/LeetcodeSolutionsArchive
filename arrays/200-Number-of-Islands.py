# Problem: https://leetcode.com/problems/number-of-islands/
# Approach: Search through matrix, when island index found use dfs to turn all adjacent island indices to 0 to remove whole connected island and incrememnt count. Final matrix should be all water ("0")
# Complexity: O(n * m) time where n is rows and m is cols, O(n * m) space (callstack)
# Enjoyment: 4/5

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs removes all adjacent 1's
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            
            if grid[r][c] == "0":
                return
            
            if grid[r][c] == "1":
                # remove island so it isn't checked again
                grid[r][c] = "0"
                
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count
