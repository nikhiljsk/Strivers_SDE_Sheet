# Approach - 1
# O(LogN), O(1)
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)

        curr = root
        while curr:
            if curr.val <= val:
                if curr.right: curr = curr.right
                else: curr.right = TreeNode(val); return root
            else:
                if curr.left: curr = curr.left
                else: curr.left = TreeNode(val); return root
        return root