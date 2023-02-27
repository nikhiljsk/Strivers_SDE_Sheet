# Approach 1
# O(2**N + Sorting), O(2**N)
def helper(self, arr, ind, summ, res):
    if ind == len(arr):
        res.append(summ)
        return
    
    # Include
    self.helper(arr, ind+1, summ+arr[ind], res)
    
    # Exclude
    self.helper(arr, ind+1, summ, res)
    
    return res


def subsetSums(self, arr, N):
    res = list()
    return self.helper(arr, 0, 0, res)

# Go - Code for Subset in unique elements array in leetcode
# func helper(nums []int, ind int, ds []int, res *[][]int) {
# 	if ind == len(nums) {
# 		*res = append(*res, ds)
# 		return
# 	}

# 	// Alias for ds, as it gets changed. Nothing else works.
# 	tDs := make([]int, len(ds))
# 	copy(tDs, ds)

# 	// Pick
# 	helper(nums, ind+1, append(ds, nums[ind]), res)

# 	// Not-Pick
# 	helper(nums, ind+1, tDs, res)
# }

# func subsets(nums []int) [][]int {
# 	var res [][]int
# 	var ds []int
# 	helper(nums, 0, ds, &res)
# 	return res
# }