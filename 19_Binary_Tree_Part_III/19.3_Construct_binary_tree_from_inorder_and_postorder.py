# Approach 1
# O(N), O(N)
class Solution:
    def helper(self, postorder, postStart, postEnd, inorder, inStart, inEnd, inMap):
        if postStart > postEnd or inStart > inEnd:
            return None

        rootVal = postorder[postEnd]
        root = TreeNode(val=rootVal)

        inRoot = inMap[rootVal]
        numsLeft = inRoot - inStart

        root.left = self.helper(postorder, postStart, postStart+numsLeft-1, inorder, inStart, inRoot-1, inMap)
        root.right = self.helper(postorder, postStart+numsLeft, postEnd-1, inorder, inRoot+1, inEnd, inMap)

        return root


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = dict()
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        root = self.helper(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, inMap)
        return root