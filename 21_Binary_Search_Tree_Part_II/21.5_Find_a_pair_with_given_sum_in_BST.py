# Approach 1 - Naive
# O(2N), O(N)
class Solution:
    def __init__(self):
        self.inorder = list()

    def helper(self, root):
        if not root: return None
        self.helper(root.left)
        self.inorder.append(root.val)
        self.helper(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.helper(root)

        i, j = 0, len(self.inorder)-1
        while i < j:
            curr_sum = self.inorder[i]+self.inorder[j]
            if curr_sum == k:
                return True
            elif curr_sum < k:
                i+=1
            else:
                j-=1
        return False


# Approach 2 - Optimal
# O(N), O(2H)
class BSTIterator:
    def __init__(self, root, reverse):
        self.stack = list()
        self.reverse = reverse
        self.pushAll(root)

    def pushAll(self, root):
        while root:
            self.stack.append(root)
            if self.reverse:
                root = root.right
            else:
                root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        if not self.reverse:
            self.pushAll(res.right)
        else:
            self.pushAll(res.left)
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0


class Solution:
    def findTarget(self, root, k):
        if not root: return False
        l = BSTIterator(root, False)
        r = BSTIterator(root, True)

        i, j = l.next(), r.next()
        while i < j:
            curr_sum = i+j
            if curr_sum == k:
                return True
            elif curr_sum < k:
                i = l.next()
            else:
                j = r.next()
        return False