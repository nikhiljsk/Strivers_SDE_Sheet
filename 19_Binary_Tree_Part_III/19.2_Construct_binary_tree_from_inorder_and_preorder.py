# Notes
# We cannot construct a unique binary tree from given Pre-order and Post-order
# Example (1, 2, 3) and (3, 2, 1) given for pre and post respectively.
# There exists a couple of tress satisfying the above conditions
# Link - https://www.youtube.com/watch?v=9GMECGQgWrQ&

# Approach 1
# O(N), O(N)
class Solution:
    def helper(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        if preStart > preEnd or inStart > inEnd:
            return None

        rootVal = preorder[preStart]
        root = TreeNode(val=rootVal)

        inRoot = inMap[rootVal]
        numsLeft = inRoot - inStart

        root.left = self.helper(preorder, preStart+1, preStart+numsLeft, inorder, inStart, inRoot-1, inMap)
        root.right = self.helper(preorder, preStart+numsLeft+1, preEnd, inorder, inRoot+1, inEnd, inMap)

        return root


    def buildTree(self, preorder, inorder):
        inMap = dict()
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        root = self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
        return root