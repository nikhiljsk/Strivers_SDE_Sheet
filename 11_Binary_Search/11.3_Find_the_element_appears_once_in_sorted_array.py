class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = l + (r-l)//2
            if (mid%2 == 0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                l = mid+1
            else:
                r = mid
        return nums[l]

# Tips
# Three templates of binary search exists, the one used above is template number 2.
# https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/935/