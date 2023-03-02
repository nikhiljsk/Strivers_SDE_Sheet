# Approach 1 - Naive
# O(1), O(N)
# Just push all elements into an array in inorder 


# Approach 2 - Optimal
# O(1), O(H) - O(1) is for the next function, even though you're pushing a few elements,
# consider the case where there are n next calls, so that makes n/n = 1
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.pushAll(root)

    def pushAll(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        res = self.stack.pop()
        if res.right:
            self.pushAll(res.right)
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0