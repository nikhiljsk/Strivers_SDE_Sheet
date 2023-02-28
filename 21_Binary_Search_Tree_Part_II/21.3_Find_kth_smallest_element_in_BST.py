# Approach 1 - Recursive
# O(min(N, K)), O(min(N, K))
class Solution:
    def __init__(self):
        self.count = 0
        self.res = -1

    def kthSmallest(self, root, k):
        if not root:
            return None
        self.kthSmallest(root.left, k)

        self.count += 1
        if self.count == k:
            self.res = root.val

        self.kthSmallest(root.right, k)
        return self.res


# Approach 2 - Iterative Traversal
# O(min(N, K)), O(min(N, K))
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, count = list(), 0
        curr = root
        while True:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) == 0:
                    break

                curr = stack.pop()
                count+=1
                if count == k:
                    return curr.val
                curr = curr.right
        return -1


# Approach 3 - Morris Traversal
# O(min(N, K)), O(1)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr, count = root, 0
        while curr:
            if not curr.left:
                count+=1
                if count == k:
                    return curr.val
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    count+=1
                    if count == k:
                        return curr.val
                    curr = curr.right
        return -1