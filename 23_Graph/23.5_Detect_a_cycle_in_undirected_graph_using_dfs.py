# Approach 1
# O(N+2E+N), O(3N)
# DFS - Detect Cycle in undirected Graph, given adjList
# GeeksforGeeks    
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

    def isCycle(self, V, adjList):
        vis = [0 for _ in range(V)]

        for i in range(V):
            if vis[i] != 1:
                if self.hasCycle(i, -1, vis, adjList):
                    return True
        return False