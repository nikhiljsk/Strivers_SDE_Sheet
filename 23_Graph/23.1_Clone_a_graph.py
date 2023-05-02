# Approach 1
# O(V+E), O(V+E)
class Solution:
    def clone(self, node, oldToNew):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(self.clone(nei, oldToNew))
        
        return copy

    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = dict()
        return self.clone(node, oldToNew) if node else None