# Approach 1
# O(N + 2E), O(2N)
class Solution:
    def canColor(self, node, V, adjList, colors):
        for nei in adjList[node]:
            if colors[nei] == -1:
                colors[nei] = int(not colors[node])
                if not self.canColor(nei, V, adjList, colors):
                    return False
            elif colors[nei] == colors[node]:
                return False
        return True


    def isBipartite(self, adjList):
        V = len(adjList)
        colors = [-1 for _ in range(V)]
        for i in range(V):
            if colors[i] == -1:
                colors[i] = 0
                if not self.canColor(i, V, adjList, colors):
                    return False
        return True