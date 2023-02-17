# Approach 1 - Morris Traversal
# O(N), O(1) - Amortized time complexity
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, res = root, list()
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    res.append(curr.val)
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return res