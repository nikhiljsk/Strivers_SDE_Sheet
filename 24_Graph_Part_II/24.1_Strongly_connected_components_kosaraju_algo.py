# Approach 1
# O(V+E), O(V+E)
# Kosaraju's Algorithm
class Solution:
    def dfs(self, node, adj, st, vis):
        vis[node] = 1
        for nei in adj[node]:
            if vis[nei] != 1:
                self.dfs(nei, adj, st, vis)
        st.append(node)

    def revdfs(self, node, adjT, vis):
        vis[node] = 1
        for nei in adjT[node]:
            if vis[nei] != 1:
                self.revdfs(nei, adjT, vis)

    def kosaraju(self, V, adj):
        vis = [0 for _ in range(V)]
        st = list()
        for i in range(V):
            if vis[i] != 1:
                self.dfs(i, adj, st, vis)

        adjT = [[] for _ in range(V)]
        for i in range(V):
            vis[i] = 0
            for nei in adj[i]:
                adjT[nei].append(i)

        res = 0
        while st:
            node = st.pop()
            if vis[node] != 1:
                self.revdfs(node, adjT, vis)
                res += 1
        return res