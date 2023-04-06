# Approach 1
# Using Recursion
# For an undirected graph, O(N) + O(2E), For a directed graph, O(N) + O(E)
# O(3N) Space
class Solution:
    def helper(self, node, vis, res, adjList):
        vis[node] = True
        res.append(node)
        
        for degree in adjList[node]:
            if degree not in vis:
                self.helper(degree, vis, res, adjList)
    
    def dfsOfGraph(self, V: int, adjList):
        res, vis = list(), dict()
        self.helper(0, vis, res, adjList)
        return res