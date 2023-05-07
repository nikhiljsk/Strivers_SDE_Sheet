# Approach 1
# O(E logE), O(E+V)
from heapq import heappop, heappush
class Solution:
    def spanningTree(self, V, adjList):
        heap = [(0,0)]
        vis = [0 for _ in range(V)]
        minSum = 0
        while heap:
            wt, node = heappop(heap)
            if vis[node] == 1:
                continue

            vis[node] = 1
            minSum += wt
            for nei in adjList[node]:
                currNode, currWt = nei[0], nei[1]
                if vis[currNode] != 1:
                    heappush(heap, (currWt, currNode))

        return minSum