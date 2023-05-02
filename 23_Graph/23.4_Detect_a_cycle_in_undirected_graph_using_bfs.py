# Approach 1 - Doesn't WORK!!
# O(N+2E+N), O(3N)
from collections import deque
class Solution:
    def detectCycle(self, node, adjList, vis):
        q = deque()

        q.append((node, -1))
        while q:
            node, parent = q.popleft()
            vis[node] = 1

            for nei in adjList[node]:
                if vis[nei] != 1:
                    vis[nei] = 1
                    self.detectCycle(nei, adjList, vis)
                elif parent != nei:
                    return True
        return False


    def createAdjList(self, vertex, edges):
        adjList = [[] for _ in range(vertex)]

        for i in range(len(edges)):
            source = edges[i][0]
            dest = edges[i][1]
            adjList[source].append(dest)

        # adjList = [sorted(x) for x in adjList]
        return adjList

    def canFinish(self, V: int, edges: List[List[int]]) -> bool:
        if V == 1: return True
        vis = [0 for _ in range(V)]
        adjList = self.createAdjList(V, edges)
        print("TEST", adjList)

        for i in range(V):
            if vis[i] != 1:
                if self.detectCycle(i, adjList, vis):
                    return True
        return False