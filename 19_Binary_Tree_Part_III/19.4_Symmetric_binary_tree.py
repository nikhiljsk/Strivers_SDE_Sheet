# Approach 1 - Recursive
# O(N), O(H)
class Solution:
    def helper(self, a, b):
        if not a or not b:
            return a == b
        if a.val != b.val: return False

        return self.helper(a.left, b.right) and \
                    self.helper(a.right, b.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        return self.helper(root.left, root.right)

# Approach 2 - Iterative
# O(N), O(W)
# Using Level order traversal without two pointers would be possible, but tricky
# You'll have to replace nil pointers with a flag value like # or something
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        q = collections.deque([(root.left, root.right),])
        while len(q) != 0:
            a, b = q.popleft()

            if not a and not b:
                continue
            elif not a or not b:
                return a == b
            if a.val != b.val:
                return False

            q.extend([(a.left, b.right), (a.right, b.left)])
        return True