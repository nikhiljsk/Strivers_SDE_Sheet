# Approach 1
# O(5*N*M), O(N*M)
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        vis = [ [0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([[i, j], 0])
                    vis[i][j] = 2
                else:
                    vis[i][j] = 0

        res = 0
        dRow = [-1, 0, 1, 0]
        dCol = [0, 1, 0, -1]
        while len(queue) != 0:
            row, col = queue[0][0][0], queue[0][0][1]
            time = queue[0][1]
            res = max(res, time)
            queue.popleft()
            for i in range(4):
                nRow = row + dRow[i]
                nCol = col + dCol[i]

                if nRow >=0 and nRow < m and nCol >= 0 and nCol < n and vis[nRow][nCol] == 0 and grid[nRow][nCol] == 1:
                    queue.append([[nRow, nCol], time+1])
                    vis[nRow][nCol] = 2

        for i in range(m):
            for j in range(n):
                if vis[i][j] != 2 and grid[i][j] == 1:
                    return -1

        return res
