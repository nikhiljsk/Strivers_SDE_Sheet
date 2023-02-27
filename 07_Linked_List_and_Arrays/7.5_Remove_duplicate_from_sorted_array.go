// Approach 1
// O(N), O(N)
// Store the non-duplicate elements in a array and then re-populate the array

// Approach 2
// O(N), O(1)
func removeDuplicates(nums []int) int {
	i := 0
	for j := 1; j < len(nums); j++ {
		if nums[i] != nums[j] {
			i++
			nums[i] = nums[j]
		}
	}
	return i + 1
}