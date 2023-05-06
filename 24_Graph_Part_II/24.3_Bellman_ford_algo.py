# Approach 1
# O(E * V), O(1)
# Works only on DAG, if a UdAG is given create two edges between nodes
class Solution:
    def bellman_ford(self, V, edges, S):
        dis = [int(1e8) for _ in range(V)]
        dis[S] = 0
        for i in range(V-1):
            for src, dst, curr_dis in edges:
                if dis[src] != 1e8 and dis[src] + curr_dis < dis[dst]:
                    dis[dst] = dis[src] + curr_dis
        
        # Detect negative cycle
        for src, dst, curr_dis in edges:
                if dis[src] != 1e8 and dis[src] + curr_dis < dis[dst]:
                    return [-1]
        
        return dis