# Approach 1 - Doesn't WORK!!
# O(N+2E+N), O(3N)
# BFS - Detect Cycle in undirected Graph, given adjList
# GeeksforGeeks
from collections import deque
class Solution:
    def detectCycle(self, node, adjList, vis):
        q = deque()

        q.append((node, -1))
        vis[node] = 1
        while q:
            node, parent = q.popleft()

            for nei in adjList[node]:
                if vis[nei] != 1:
                    vis[nei] = 1
                    q.append((nei, node))
                elif parent != nei:
                    return True
        return False

    def isCycle(self, V, adjList):
        vis = [0 for _ in range(V)]

        for i in range(V):
            if vis[i] != 1:
                if self.detectCycle(i, adjList, vis):
                    return True
        return False