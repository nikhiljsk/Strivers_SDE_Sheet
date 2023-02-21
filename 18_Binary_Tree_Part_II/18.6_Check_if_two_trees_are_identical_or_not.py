# Approach 1 - Recursive
# O(N), O(H)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q

        sameSoFar = (p.val == q.val)

        return sameSoFar and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Approach 2 - Iterative
# The trick here is to store the null values in the queue, if you ignore them it will be wrong
# Consider [1, null, 2] and [1, 2, null] - If you don't store null it will be True and that's wrong
# O(N), O(N)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q = collections.deque([(p, q)])
        while len(q) != 0:
            i, j = q.popleft()
            if not i and not j:
                continue
            if not i or not j:
                return False
            if i.val != j.val:
                return False

            q.append([i.left, j.left])
            q.append([i.right, j.right])
        return True
