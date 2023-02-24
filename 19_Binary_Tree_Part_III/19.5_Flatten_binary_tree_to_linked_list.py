# Approach 1 - Recursive
# O(N), O(N)
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


# Approach 2 - Iterative
# O(N), O(N)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return

        curr, s = root, list([root])
        while len(s) != 0:
            curr = s.pop()
            if curr.right: s.append(curr.right)
            if curr.left: s.append(curr.left)

            if len(s) != 0: # Need to check the size of the stack, cause for the last node it might cause issues
                curr.right = s[-1]
                curr.left = None


# Approach 3 - Similar to Morris Traversal
# O(N), O(1)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev and prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right