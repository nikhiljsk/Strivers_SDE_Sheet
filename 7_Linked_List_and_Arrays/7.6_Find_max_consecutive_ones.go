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