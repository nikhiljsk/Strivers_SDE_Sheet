# Approach 1
# Using the DFS method for topological sort is the easiest
# O(N+E), O(N)
class Solution:
    def dfs(self, node, vis, stack, adjList):
        vis[node] = 1
        for nei in adjList[node]:
            if vis[nei] != 1:
                self.dfs(nei, vis, stack, adjList)
        stack.append(node)


    def topoSort(self, V, adjList):
        vis = [0 for _ in range(V)]
        stack, res = list(), list()

        for i in range(V):
            if vis[i] != 1:
                self.dfs(i, vis, stack, adjList)

        while stack:
            res.append(stack.pop())
        return res