# Approach 1 - Using Adj List
# For a directed graph, given the number of Nodes (0 to N-1) and adjacency List
# Also given to IGNORE nodes with no connections
# O(N + 2E), O(2N) - Since every node and all degrees associated with it, Since Queue and Visited
from collections import deque
class Solution:
    def bfsOfGraph(self, V: int, adj):
        res, vis = list(), dict()
        q = deque()

        q.append(0)
        while q:
            curr = q.popleft()
            res.append(curr)
            vis[curr] = True

            for degree in adj[curr]:
                if degree not in vis:
                    vis[degree] = True
                    q.append(degree)
        return res


# Approach 2 - Using Adj List
# For an undirected graph, given the number of nodes (0 to N-1) and Edges in the form of two lists, src and dest
# Also given to consider nodes with no edges, and a specific order
# O(N + 2E), O(2N)
from collections import deque
def BFSHelper(adj, i, vis):
    q = deque()
    res = list()

    q.append(i)
    while q:
        curr = q.popleft()
        res.append(curr)
        vis[curr] = True

        for degree in adj[curr]:
            if degree not in vis:
                vis[degree] = True
                q.append(degree)
    return res


def createAdjList(vertex, edges):
    adjList = [[] for _ in range(vertex)]

    for i in range(len(edges[0])):
        source = edges[0][i]
        dest = edges[1][i]
        adjList[source].append(dest)
        adjList[dest].append(source)

    adjList = [sorted(x) for x in adjList]
    return adjList


def BFS(vertex, edges):
    res = list()
    adj = createAdjList(vertex, edges)
    vis = dict()

    for i in range(vertex):
        if i not in vis:
            res.extend(BFSHelper(adj, i, vis))

    return res


# Approach 3 - Using Adj Matrix
# For an undirected graph, given the number of nodes (0 to N-1) and Edges in the form of two lists, src and dest
# Also given to consider nodes with no edges, and a specific order
# O(N+E), O(N2)
result = []

def BFSHelper(edges, source, visited):
    queue = []
    visited[source] = True
    queue.append(source)
    while len(queue) != 0:
        front = queue.pop(0)
        result.append(front)
        for i in range(len(edges)):
            if edges[front][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


def createAdjMat(vertex, edges):
    adjacency_matrix = [[0] * vertex for _ in range(vertex)]
    for i in range(len(edges[0])):
        adjacency_matrix[edges[0][i]][edges[1][i]] = 1
        adjacency_matrix[edges[1][i]][edges[0][i]] = 1
    return adjacency_matrix


def BFS(vertex, edges):
    adjacency_matrix = createAdjMat(vertex, edges)
    visited = [False] * len(adjacency_matrix)
    for i in range(len(visited)):
        if not visited[i]:
            BFSHelper(adjacency_matrix, i, visited)
    return result