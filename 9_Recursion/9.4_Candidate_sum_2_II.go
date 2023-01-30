// Approach 1
// Similar to subset 2, just calculate all unique subsets
// O(2**N), O(Number of combinations)
func helper(nums []int, target, ind int, ds []int, res *[][]int) {
	if target == 0 {
		tmp := make([]int, len(ds))
		copy(tmp, ds)
		*res = append(*res, tmp)
		return
	}

	for i := ind; i < len(nums); i++ {
		if i != ind && nums[i] == nums[i-1] {
			continue
		}
		if nums[i] > target {
			break
		}
		ds = append(ds, nums[i])
		helper(nums, target-nums[i], i+1, ds, res)
		ds = (ds)[:len(ds)-1]
	}
}

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	res := make([][]int, 0)
	ds := make([]int, 0)
	helper(candidates, target, 0, ds, &res)
	return res
}