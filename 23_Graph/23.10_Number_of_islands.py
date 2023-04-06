# Approach 1
# Using Grid approach with DFS
# O(2 * N2), O(4 * N2)
class Solution(object):
    def dfs(self, i, j, vis, grid):
        R, C = len(grid), len(grid[0])

        if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] == '0' or vis[i][j] == 1:
            return

        vis[i][j] = 1
        self.dfs(i + 1, j, vis, grid)
        self.dfs(i - 1, j, vis, grid)
        self.dfs(i, j + 1, vis, grid)
        self.dfs(i, j - 1, vis, grid)

    def numIslands(self, grid):
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        vis = [[0 for _ in range(C)] for _ in range(R)]

        count = 0
        for i in range(R):
            for j in range(C):
                if vis[i][j] == 0 and grid[i][j] == '1':
                    self.dfs(i, j, vis, grid)
                    count += 1
        return count

# Follow up - If 8 directional
# O(2 * N2), O(9 * N2)
class Solution(object):
    def dfs(self, i, j, vis, grid):
        R, C = len(grid), len(grid[0])

        if i < 0 or i >= R or j < 0 or j >= C or grid[i][j] == 0 or vis[i][j] == 1:
            return

        vis[i][j] = 1

        for delrow in range(-1, 2):
            for delcol in range(-1, 2):
                ni, nj = i+delrow, j+delcol
                self.dfs(ni, nj, vis, grid)


    def numIslands(self, grid):
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        vis = [[0 for _ in range(C)] for _ in range(R)]

        count = 0
        for i in range(R):
            for j in range(C):
                if vis[i][j] == 0 and grid[i][j] == 1:
                    self.dfs(i, j, vis, grid)
                    count += 1
        return count
