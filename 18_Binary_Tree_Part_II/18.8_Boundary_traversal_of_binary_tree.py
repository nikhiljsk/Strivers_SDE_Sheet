# Approach 1
# O(N),O(N) - Mutliple Traversal
class Solution:
    def isLeaf(self, root):
        if not root.left and not root.right:
            return True
        return False

    def leftNodes(self, curr, res):
        while curr:
            if not self.isLeaf(curr): res.append(curr.data)
            if curr.left: curr = curr.left
            else: curr = curr.right

    def leafNodes(self, curr, res):
        if self.isLeaf(curr):
            res.append(curr.data)
            return
        if curr.left: self.leafNodes(curr.left, res)
        if curr.right: self.leafNodes(curr.right, res)

    def rightNodes(self, curr, res):
        stack = list()
        while curr:
            if not self.isLeaf(curr): stack.append(curr.data)
            if curr.right: curr = curr.right
            else: curr = curr.left
        while len(stack) != 0:
            res.append(stack.pop())


    def printBoundaryView(self, root):
        res = list()
        if not root: return res
        if not self.isLeaf(root): res.append(root.data)

        self.leftNodes(root.left, res)
        self.leafNodes(root, res)
        self.rightNodes(root.right, res)

        return res