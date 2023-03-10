// Approach 1
// O(N), O(1)
func findMaxConsecutiveOnes(nums []int) int {
	local, global := 0, 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			local = 0
		} else {
			local++
		}
		if global < local {
			global = local
		}
	}
	return global
}

// Python Code
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, g = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l = 0
            else:
                l+=1
            g = max(l, g)
        return g
"""