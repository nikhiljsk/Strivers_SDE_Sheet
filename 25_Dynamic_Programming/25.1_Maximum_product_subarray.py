# Approach 1
# O(N), O(1)
# Idea here is to keep track of the min and max product so far,
# As negative numbers exists, someitmes min * currNumber gives us maximum product
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax, res = 1, 1, max(nums) # Res has to ben max(nums), as just a negative number can be the answer
        for num in nums:
            cand = [num, currMin * num, currMax * num]
            currMin = min(cand)
            currMax = max(cand)
            res = max(res, currMax)
        return res
