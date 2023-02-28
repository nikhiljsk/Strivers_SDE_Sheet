# Approach 1
# O(N), O(N)
class Solution:
    def helper(self, root, low, high):
        if not root: return True
        if root.val <= low or root.val >= high: return False
        return self.helper(root.left, low, root.val) and \
            self.helper(root.right, root.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('+inf'))