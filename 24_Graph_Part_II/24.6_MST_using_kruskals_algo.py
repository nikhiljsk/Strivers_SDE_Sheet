# Approach 1
# Using DisjointSet
# O(N+E) + O(E logE) + O(E*4α*2), O(2N + E)
class DisjointSet:
    def __init__(self, V):
        self.rank = [0 for _ in range(V)]
        self.size = [1 for _ in range(V)]
        self.par = [i for i in range(V)]

    def findPar(self, node):
        if node == self.par[node]:
            return node
        self.par[node] = self.findPar(self.par[node])
        return self.par[node]

    def unionByRank(self, u, v):
        ulp_u = self.findPar(u)
        ulp_v = self.findPar(v)

        if ulp_v == ulp_u:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.par[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.par[ulp_v] = ulp_u
        else:
            self.par[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findPar(u)
        ulp_v = self.findPar(v)

        if ulp_v == ulp_u:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.par[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.par[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def spanningTree(self, V, adj):
        edges = list()
        for node in range(V):
            for adjNode, wt in adj[node]:
                edges.append((wt, node, adjNode))

        ob = DisjointSet(V)
        edges.sort()
        res = 0

        for wt, node, adjNode in edges:
            if ob.findPar(node) != ob.findPar(adjNode):
                res += wt
                ob.unionByRank(node, adjNode)

        return res
    

# Driver Code for Disjoint Set
ob = DisjointSet(4)
ob.unionByRank(0, 1)
ob.unionByRank(2,3)
print("1 and 3 both in same?", ob.findPar(1) == ob.findPar(2))
ob.unionByRank(1,2)
print("1 and 3 both in same?", ob.findPar(1) == ob.findPar(2))