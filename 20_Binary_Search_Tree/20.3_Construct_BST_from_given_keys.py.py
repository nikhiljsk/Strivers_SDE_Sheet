# Approach 1 - Recursive
# O(N), O(N)
class Solution:
    def helper(self, nums, start, end):
        if start <= end:
            mid = (start + end) >> 1
            node = TreeNode(nums[mid])
            node.left = self.helper(nums, start, mid-1)
            node.right = self.helper(nums, mid+1, end)
            return node


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums)-1)