# Approach 1
# O(4^(m*n)), O(m*n)
class Solution:
    def isValid(self, row, col, m, n):
            
        if (row >= 0 and row < n and col >= 0 and col < n and m[row][col] == 1):
            return True
    
        return False
    
        
    def findPathHelper(self, m, n, x, y, dx, dy, path, res):
        if (x == n - 1 and y == n - 1):
            res.append(path)
            return
    
        dir = "DLRU"
        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if (self.isValid(row, col, m, n)):
                m[row][col] = 2             # used to track visited cells of matrix
                self.findPathHelper(m, n, row, col, dx, dy, path + dir[i], res)
                m[row][col] = 1             # mark it unvisited yet explorable
            
    def findPath(self, m,n):
        # dx, dy will be used to follow `DLRU` exploring approach
        # which is lexicographically sorted order
        dx = [ 1, 0, 0, -1 ]
        dy = [ 0, -1, 1, 0 ]
        res = []
        if (m[0][0] == 1):
            m[0][0] = 2
            self.findPathHelper(m, n, 0, 0, dx, dy, "", res)
    
        return res