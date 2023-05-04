# Approach 1
# O(N+2E+N), O(3N)
# BFS - Topological sort
from collections import deque
class Solution:
     def getInDegree(self, V, adjList):
        indeg = [0 for _ in range(V)]
        for i in range(V):
            for v in adjList[i]:
                indeg[v] += 1
        return indeg
     def topoSort(self, V, adjList):
        indeg = self.getInDegree(V, adjList)
        q = deque()
        res = []

        # Insert into q for indeg == 0
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q.pop()
            indeg[node] -= 1
            res.append(node)

            for nei in adjList[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return res