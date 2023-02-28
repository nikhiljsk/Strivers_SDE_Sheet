# Approach 1 - Recursive
# O(min(N, K)), O(min(N, K))
# Idea is to use reverse inorder
class Solution:
    def __init__(self):
        self.count = 0
        self.res = -1

    def kthLargest(self, root, k):
        if not root:
            return None
        self.kthLargest(root.right, k)

        self.count += 1
        if self.count == k:
            self.res = root.data

        self.kthLargest(root.left, k)
        return self.res


# Approach - 2 - Morris Traversal
# O(N), O(1)
# Count and find
class Solution:
    def countNodes(self, root):
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def kthLargest(self, root, k):
        n = self.countNodes(root)
        curr, count = root, 0
        while curr:
            if not curr.left:
                count+=1
                if count == n-k+1:
                    return curr.data
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
                    if count == n-k+1:
                        return curr.data
                    curr = curr.right
        return -1