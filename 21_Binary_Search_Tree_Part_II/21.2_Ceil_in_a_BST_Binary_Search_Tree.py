# Approach 1
# O(LogN), O(1)
class Solution:
    def findCeil(self,root, inp):
        ceil = -1
        while root:
            if inp == root.key:
                return root.key

            if root.key > inp:
                ceil = root.key
                root = root.left
            else:
                root = root.right
        return ceil