# Approach 1 - Almost Own Solution :)
# O(N), O(H)
class Solution:
    def __init__(self):
        self.res = float('-inf')

    def helper(self, root):
        if not root: return 0
        ls = self.helper(root.left)
        rs = self.helper(root.right)
        sum_at_node = ls + root.val + rs
        self.res = max(self.res, sum_at_node)

        temp = max(ls, rs)
        return max(root.val + temp, 0)
        # Here it is important to return only one of the max(ls, rs),
        # Since if you return both, it means you're considering the entire subtree,
        # But ideally you're only dealing with a single path/diameter of the tree. Hence you return
        # only one of ls or rs and also maybe a 0 if the answer is negative, so that you could exclude the
        # entire sub-tree

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.res

