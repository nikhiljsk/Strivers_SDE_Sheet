// Approach 1
// Similar to Subset Sums, just pick and not pick. But while picking don't increment
// O(2**N), O(Number of combinations)
func helper(candidates []int, target int, ind int, ds []int, res *[][]int) {
	if ind == len(candidates) {
		if target == 0 {
			*res = append(*res, ds)
		}
		return
	}

	// Alias for ds, as it gets changed. Nothing else works.
	tDs := make([]int, len(ds))
	copy(tDs, ds)

	// Pick
	if candidates[ind] <= target {
		helper(candidates, target-candidates[ind], ind, append(ds, candidates[ind]), res)
	}

	// Not-Pick
	helper(candidates, target, ind+1, tDs, res)
}

func combinationSum(candidates []int, target int) [][]int {
	var res [][]int
	var ds []int
	helper(candidates, target, 0, ds, &res)
	return res
}

"""
// Python Code
class Solution:
    def helper(self, nums, target, ind, ds, res):
        if ind == len(nums):
            if target == 0:
                res.append(ds.copy())
            return

        # Pick
        temp = ds.copy()
        if nums[ind] <= target:
            ds.append(nums[ind])
            self.helper(nums, target-nums[ind], ind, ds, res)

        # Not Pick
        self.helper(nums, target, ind+1, temp, res)


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, ds = list(), list()
        self.helper(candidates, target, 0, ds, res)
        return res
"""