// Approach 1 - Brute Force - TLE!
// Python Code
"""
class Solution:
    def helper(self, nums, target, ind, ds, res):
        if ind == len(nums):
            if target == 0:
                ds.sort()
                res.add(tuple(ds))
            return

        # Pick
        temp = ds.copy()
        if nums[ind] <= target:
            ds.append(nums[ind])
            self.helper(nums, target-nums[ind], ind+1, ds, res)

        # Not Pick
        self.helper(nums, target, ind+1, temp, res)


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, res, ds = list(), set(), list()
        self.helper(candidates, target, 0, ds, res)
        for i in res:
            ans.append(list(i))

        return ans
"""


// Approach 2
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

"""
// Python Code
class Solution:
    def helper(self, nums, target, ind, ds, res):
        if target == 0:
            res.append(ds.copy())
            return

        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i-1]:
                continue

            temp = ds.copy()
            if nums[i] <= target:
                ds.append(nums[i])
                self.helper(nums, target-nums[i], i+1, ds, res)
                ds.pop()



    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, ds = list(), list()
        candidates.sort()
        self.helper(candidates, target, 0, ds, res)
        return res
"""
