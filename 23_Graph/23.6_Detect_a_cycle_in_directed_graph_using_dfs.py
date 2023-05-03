# Approach 1
# O(N+2E+N), O(3N)
# DFS - Detect NO Cycle in directed Graph, given edges
# Leetcode 207
class Solution:
    def hasCycle(self, node, parent, vis, adjList):
        vis[node] = 1 
        for nei in adjList[node]:
            if vis[nei] != 1:
                if self.hasCycle(nei, node, vis, adjList):
                    return True
            elif nei != parent:
                return True
        return False

    def getAdjList(self, V, edges):
        adj = [[] for _ in range(V)]

        for c1, c2 in edges:
            adj[c1].append(c2)
        return adj

    def canFinish(self, V, edges):
        adjList = self.getAdjList(V, edges)
        vis = [0 for _ in range(V)]
        print("TEST", adjList)

        for i in range(V):
            if vis[i] != 1:
                if self.hasCycle(i, -1, vis, adjList):
                    return False
        return True
        