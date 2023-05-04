# Approach 1
# O(N+2E+N), O(3N)
# BFS - Detect NO Cycle in directed Graph, given edges, based on topological sort
# Leetcode 207
from collections import deque

class Solution:
    def getInDegree(self, V, adjList):
        indeg = [0 for _ in range(V)]
        for i in range(V):
            for v in adjList[i]:
                indeg[v] += 1
        return indeg 

    def getAdjList(self, V, edges):
        adj = [[] for _ in range(V)]

        for c1, c2 in edges:
            adj[c1].append(c2)
        return adj

    def canFinish(self, V, edges):
        adjList = self.getAdjList(V, edges)
        indeg = self.getInDegree(V, adjList)
        q = deque()
        res = 0
        
        # Insert into q for indeg == 0
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            node = q.pop()
            indeg[node] -= 1
            res += 1

            for nei in adjList[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
                
        if res == V:
            return True
        return False