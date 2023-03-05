// Approach 1
// O(N), O(1)
func nextPermutation(nums []int) {
	i, j := len(nums)-1, len(nums)-1
	// From the back, find the element that breaks ascending order
	for i > 0 && nums[i-1] >= nums[i] {
		i--
	}

	// If no break found, that means to reverse
	if i == 0 {
		reverse(nums, 0)
		return
	}

	// From the back, find the element that is greater than nums[i]
	k := i - 1
	for j > 0 && nums[k] >= nums[j] {
		j--
	}

	// Swap both
	nums[k], nums[j] = nums[j], nums[k]

	reverse(nums, k+1)
}

func reverse(nums []int, start int) {
	i := start
	j := len(nums) - 1
	for i < j {
		nums[i], nums[j] = nums[j], nums[i]
		i++
		j--
	}
}

// Approach - No
// Implementation - No - Forgot the Equal to signs.
// TODO Followup
// Implement the brute force approach of generating all permutations