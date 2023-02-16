# Approach 1 - Recursive
# O(N), O(N)
class Solution:
    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        self.helper(root, res)
        return res


# Approach 2 - Iterative - Using Two stacks
# O(N), O(2N)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:    return root

        s1, s2, res = list(), list(), list()
        s1.append(root)
        while len(s1) != 0:
            curr = s1.pop()
            s2.append(curr.val)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)

        while len(s2) != 0:
            res.append(s2.pop())

        return res


# Approach 3 - Iterative - Using one stack
# O(2N), O(N)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root

        curr, stack, res = root, list(), list()
        while curr or len(stack) != 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if temp:
                    curr = temp
                else:
                    temp = stack.pop()
                    res.append(temp.val)
                    while len(stack) != 0 and temp == stack[-1].right:
                        temp = stack.pop()
                        res.append(temp.val)

        return res
