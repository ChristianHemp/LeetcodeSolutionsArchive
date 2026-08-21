# Problem: https://leetcode.com/problems/rotting-oranges/
# Approach: First loop through grid to update fresh_count with the number of fresh oranges and adding the rotting orange indices to the queue to begin multi-starting-point bfs.
#           Check various edge cases, then initiate bfs with all rotten fruit as starting points until all possible oranges have been updated as rotten while incrementing minutes as the bfs level/length
#           If not all fresh oranges turned rotten, return -1, otherwise reutrn the number of minutes
# Complexity: O(n * m) time, O(n * m) space where n is rows and m is cols
# Enjoyment: 4/5

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        minutes = 0
        fresh_count = 0
        neighbor_directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # no fresh oranges in matrix
        if fresh_count == 0:
            return 0
        
        # no rotten oranges in matrix
        if not q:
            return -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in neighbor_directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr < 0 or nc < 0 or
                        nr >= rows or nc >= cols or
                        grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue

                    grid[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc))
            # prevents minutes from incrementing when bfs complete
            if q:
                minutes += 1
        
        # not all fresh oranges turned rotten
        if fresh_count != 0:
            return -1

        return minutes
