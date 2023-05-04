# 200. Number of Islands | Medium #Graphs #DFS

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        totalIslands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    totalIslands += 1
                    self.dfs(grid, n, m, i, j)
        
        return totalIslands

    
    def dfs(self, grid, n, m, i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == "0":
            return

        if grid[i][j] == "1":
            grid[i][j] = "0" #make it visited

        
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]

        for k in range(4):
            self.dfs(grid, n, m, i + x[k], j + y[k])


# TC : O(N.M)
# SC : O(N.M)
