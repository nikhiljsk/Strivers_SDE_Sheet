// Approach 1
// Naive Approach - For each i, check if i+j == target
// O(N2), O(1)

// Approach 2
// Sort the array, use two pointers, start and end.
// O(N * LogN), O(1)

// Approach 3
// O(N), O(N)
func twoSum(nums []int, target int) []int {
	find := make(map[int]int)
	for i, v := range nums {
		if j, ok := find[v]; ok && i != j {
			return []int{j, i}
		}
		find[target-v] = i
	}
	return []int{}
}