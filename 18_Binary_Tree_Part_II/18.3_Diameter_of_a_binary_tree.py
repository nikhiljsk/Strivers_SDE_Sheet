# Approach 1
# Caculate the height at each node, and then take max of height(left) + height(right)
# O(N), O(H)
class Solution:
    def __init__(self):
        self.res = 0


    def helper(self, root):
        if not root: return 0
        lh = self.helper(root.left)
        rh = self.helper(root.right)
        self.res = max(self.res, lh+rh)
        return 1 + max(lh, rh)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res