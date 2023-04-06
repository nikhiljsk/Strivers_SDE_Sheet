# Approach 1
# Using Adj Matrix
# O(N) + O(V+2E), Where O(N) is for outer loop and inner loop runs in total a single DFS over entire graph, and we know DFS takes a time of O(V+2E).
# O(2N)
class Solution:
    def dfs(self, node, vis, M):
        vis[node] = 1
        for j in range(len(M)):
            if M[node][j] == 1 and vis[j] == 0:
                self.dfs(j, vis, M)


    def findCircleNum(self, M: List[List[int]]) -> int:
        res, vis = 0, [0 for _ in range(len(M))]
        for i in range(len(M)):
            if vis[i] == 0:
                self.dfs(i, vis, M)
                res+=1
        return res