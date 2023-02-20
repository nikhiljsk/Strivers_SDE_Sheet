# Approach 1 - Cleaner code with class variable
# O(N), O(H)
class Solution:
    def __init__(self):
        self.res = True

    def helper(self, root):
        if not root: return 0
        lh = self.helper(root.left)
        rh = self.helper(root.right)
        if abs(rh-lh) > 1:
            self.res = False
        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.res

# Approach 1 - No class variable allowed
# O(N), O(H)
class Solution:
    def helper(self, root):
        if not root: return 0

        lh = self.helper(root.left)
        if lh == -1: return -1

        rh = self.helper(root.right)
        if rh == -1: return -1

        if abs(rh-lh) > 1: return -1

        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.helper(root) >= 0)