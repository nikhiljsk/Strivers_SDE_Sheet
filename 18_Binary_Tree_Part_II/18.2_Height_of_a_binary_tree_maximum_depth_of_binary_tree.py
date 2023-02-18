# Approach 1 - Own Approach
# O(N), O(H)
class Solution:
    def helper(self, root, level):
        if not root:
            return level

        lev1 = self.helper(root.left, level+1)
        lev2 = self.helper(root.right, level+1)

        return max(lev1, lev2)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)


# Approach 2 - Cleaner code
# O(N), O(H)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lev1 = self.maxDepth(root.left)
        lev2 = self.maxDepth(root.right)
        return 1 + max(lev1, lev2)

# Approach 3 - Iterative
# O(N), O(W)
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q, count = deque([root]), 0
        while len(q) != 0:
            qLen = len(q)
            count += 1
            for i in range(qLen):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return count