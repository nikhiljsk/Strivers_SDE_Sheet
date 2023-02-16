# Approach 1 - Recursive
# O(N), O(N)
class Solution:
    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        self.helper(root, res)
        return res


# Approach 2 - Iterative
# O(N), O(N)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = list(), list()
        curr = root
        while True:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    break

                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res
