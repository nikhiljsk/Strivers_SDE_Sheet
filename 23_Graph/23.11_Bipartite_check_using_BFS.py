# Approach 1
# O(N + 2E), O(2N)
from collections import deque
class Solution:
    def canColor(self, start, V, adjList, colors):
        q = deque()
        q.append(start)
        colors[start] = 0

        while q:
            node = q.pop()
            for nei in adjList[node]:
                if colors[nei] == -1:
                    colors[nei] = int(not colors[node])
                    q.append(nei)
                elif colors[nei] == colors[node]:
                    return False
        return True


    def isBipartite(self, adjList):
        V = len(adjList)
        colors = [-1 for _ in range(V)]
        for i in range(V):
            if colors[i] == -1:
                if not self.canColor(i, V, adjList, colors):
                    return False
        return True