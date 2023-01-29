// Approach 1 - FAILED to implement! (Hashmap not implemented)
// The following code generates all subsets
// Generate all subsets, put it into hashmap for de-duplication
// O(2**N) * LogN - Since putting in hashmap takes time
// O(2**N)
func helper(arr []int, ind int, sub []int, res *[][]int) {
	if len(arr) == ind {
		*res = append(*res, sub)
		return
	}

	// Include
	subInclude := append(sub, arr[ind])
	helper(arr, ind+1, subInclude, res)

	// Exclude
	helper(arr, ind+1, sub, res)
}

func subsetsWithDup(nums []int) [][]int {
	res := make([][]int, 0)
	helper(nums, 0, []int{}, &res)
	return res
}

// Approach 2
// For each level of recursion generate subsets so that each length of subsets are covered.
// For level 1 generate 1-lenght subsets, for 2 generate 2-length subsets and so on.
// Also avoid duplication incase of already picked in current level, hence i!=ind
func helper(nums []int, ind int, ds []int, res *[][]int) {
	// Add the completed subset
	tmp := make([]int, len(ds))
	copy(tmp, ds)
	*res = append(*res, tmp)

	// Iterate from ind to n-1, to create subsets of length level
	for i := ind; i < len(nums); i++ {
		// Ignore duplication
		if i != ind && nums[i] == nums[i-1] {
			continue
		}
		// Insert the element
		ds = append(ds, nums[i])
		// Recursion
		helper(nums, i+1, ds, res)
		// Pop element
		ds = (ds)[:len(ds)-1]
	}
	// Base case is not necessary cause of primary for loop running till N
}

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)
	ds := make([]int, 0)
	helper(nums, 0, ds, &res)
	return res
}