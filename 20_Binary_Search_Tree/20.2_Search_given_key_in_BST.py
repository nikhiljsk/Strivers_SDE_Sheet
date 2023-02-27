# Approach 1 - Iterative
# O(LogN), O(1)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if root.val < val: root = root.right
            else: root = root.left
        return root


# Approach 2 - Recursive
# O(LogN), O(LogN)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val==val:
            return root
        if root.val<val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)