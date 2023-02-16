# Approach 1 - Recursive
# O(N), O(N)
class Solution:
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        self.helper(root, res)
        return res


# Approach 2 - Iterative
# O(N), O(N)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        
        stack, res = list(), list()
        stack.append(root)
        curr = root
        while len(stack) != 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res