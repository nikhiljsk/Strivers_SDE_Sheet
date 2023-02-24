# Approach 1 - Recursive
# O(N), O(N)
# Here the order doesn't matter, you could swap and then call left or right or vice-versa
class Solution:
    def mirror(self,root):
        if not root: return
        self.mirror(root.left)
        self.mirror(root.right)
        root.left, root.right = root.right, root.left


# Approach 2 - Iterative
# O(N), O(N)
class Solution:
    def mirror(self,root):
        if not root: return
        s = list([root])
        while len(s) != 0:
            curr = s.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left: s.append(curr.left)
            if curr.right: s.append(curr.right)

# TODO:
# https://www.codingninjas.com/codestudio/problems/invert-a-binary-tree_1281382