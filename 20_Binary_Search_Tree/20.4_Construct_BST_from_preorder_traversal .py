# Approach 1
# O(N2), O(1)
# Use a while loop to find the right place of every node in preorder and then place it


# Approach 2
# O(NLogN), O(N)
# Sort the preorder to get an inorder. Now you have pre and in order. Just follow the previous process


# Approach 3
# O(3N), O(N)
class Solution:
    def __init__(self):
        self.ind = 0

    def helper(self, preorder, bound):
        if self.ind == len(preorder) or preorder[self.ind] >= bound:
            return None

        root = TreeNode(preorder[self.ind])
        self.ind += 1

        root.left = self.helper(preorder, root.val)
        root.right = self.helper(preorder, bound)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, float("+inf"))