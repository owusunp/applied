"""
LeetCode #200 - Number of Islands

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: empty grid has no islands
        if not grid:
            return 0
        
        # Get dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Set to track visited cells (prevents infinite loops)
        visit = set()
        # Counter for number of islands found
        islands = 0
        
        def bfs(r, c):
            # Create queue for BFS traversal
            q = collections.deque()
            # Add starting cell to queue and mark as visited
            q.append((r, c))
            visit.add((r, c))
         
            
            # Process queue until empty
            while q:
                # Get next cell from front of queue
                row, col = q.popleft()
                # Define 4 directions: down, up, right, left
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                # Check all 4 neighbors
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check bounds, land cell, and not visited
                    if (r in range(rows) and c in range(cols) and 
                        grid[r][c] == "1" and (r, c) not in visit):
                        # Add valid neighbor to queue and mark as visited
                        q.append((r, c))
                        visit.add((r, c))
        
        # Scan entire grid for unvisited land cells
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not visited, start BFS
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Explore entire island with BFS
                    bfs(r, c)
                    # Increment island count
                    islands += 1
        
        # Return total number of islands
        return islands
