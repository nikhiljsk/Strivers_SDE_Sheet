# Approach 1 - Own Solution and Brute Force
# O(3N), O(2H+2N)
class Solution:
    def findPath(self, root, target, res):
        if not root: return False

        res.append(root)
        if root == target: return True

        if self.findPath(root.left, target, res) or self.findPath(root.right, target, res):
            return True

        res.pop()
        return False


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1, path2 = list(), list()
        self.findPath(root, p, path1)
        self.findPath(root, q, path2)

        for i in range(len(path1)-1, -1, -1):
            for j in range(len(path2)):
                if path1[i] == path2[j]:
                    return path1[i]

        return root


# Approch 2 - Optimal
# O(N), O(H)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root
