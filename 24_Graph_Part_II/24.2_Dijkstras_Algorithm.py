# Approach 1
# Using minHeap
# O(E Log V), O(V)
# Imp to store the first key in tuple as distance, as heap is maintained based on that
# Does not work on negative weights or cycles
from heapq import heappop, heappush
class Solution:
    def dijkstra(self, V, adjList, src):
        heap = [(0, src)]
        dis = [float('inf') for _ in range(V)]
        dis[src] = 0
        
        while heap:
            curr_dis, node = heappop(heap)
            
            for nei in adjList[node]:
                adjNode = nei[0]
                edgeWeight = nei[1]
                
                if curr_dis + edgeWeight < dis[adjNode]:
                    dis[adjNode] = curr_dis + edgeWeight
                    heappush(heap, (dis[adjNode], adjNode))
            
        return dis

# Follow-up question - Print the shortest path
# Approach 1
# Using minHeap
# O(E Log V), O(V)
# GFG Link: https://practice.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1
# Does not work on negative weights or cycles
from heapq import heappop, heappush
class Solution:
    def getAdjList(self, V, edges):
        adj = [[] for _ in range(V+1)]
        for c1, c2, c3 in edges:
            adj[c1].append((c3,c2))
            adj[c2].append((c3,c1))
        return adj
    
    def shortestPath(self, V, E, edges):
        adjList = self.getAdjList(V, edges)
        heap = [(0, 1)]
        dis = [float('inf') for _ in range(V+1)]
        par = [i for i in range(V+1)]
        dis[1] = 0
        while heap:
            curr_dis, node = heappop(heap)
            for nei in adjList[node]:
                adjNode = nei[1]
                edgeWeight = nei[0]
                
                if curr_dis + edgeWeight < dis[adjNode]:
                    dis[adjNode] = curr_dis + edgeWeight
                    par[adjNode] = node
                    heappush(heap, (dis[adjNode],adjNode))

        if dis[V] == float('inf'): return [-1]
        
        node = V
        path = []
        while par[node] != node:
            path.append(node)
            node = par[node]
        path.append(1)
        
        return list(reversed(path))