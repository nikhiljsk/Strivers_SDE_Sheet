# Approach 1 - Naive
# O(N), O(N)
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

# Approach 2 - Recursive
# O(H), O(H)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        if root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestor(root.left, p, q)
        return root


# Approach 3 - Iterative
# O(H), O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root

        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
        return -1