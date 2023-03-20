// Approach 1
// Using a map to see to that all nums are used to gen all permutations
// O(N! * N), O(2N)
func helper(nums, ds []int, found map[int]bool, res *[][]int) {
    if len(ds) == len(nums) {
        tmp := make([]int, len(ds))
        copy(tmp, ds)
        *res = append(*res, tmp)
        return
    }
    for i:=0; i<len(nums); i++{
        if _, ok := found[nums[i]]; !ok {
            ds = append(ds, nums[i])
            found[nums[i]] = true
            helper(nums, ds, found, res)
            delete(found, nums[i])
            ds = ds[:len(ds)-1]
        }
    }
}

func permute(nums []int) [][]int {
    var res [][]int
    var ds []int
    found := make(map[int]bool)
    helper(nums, ds, found, &res)
    return res
}

"""
// Python Code
class Solution:
    def helper(self, nums, ind, ds, res, found):
        if len(ds) == len(nums):
            res.append(ds.copy())
            return
        for i in range(len(nums)):
            if nums[i] not in found:
                found[nums[i]] = True
                ds.append(nums[i])
                self.helper(nums, i+1, ds, res, found)
                ds.pop()
                del found[nums[i]]


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        found = dict()
        self.helper(nums, 0, [], res, found)
        return res

"""

// Approach 2
// Intelligently using swapping
// O(N! * N), O(1) - If we ignore stack level N, and also result N!
func helper(nums []int, ind int, res *[][]int) {
    if ind == len(nums){
        tmp := make([]int, len(nums))
        copy(tmp, nums)
        *res = append(*res, tmp)
        return
    }
    for i:=ind; i<len(nums); i++ {
        nums[i], nums[ind] = nums[ind], nums[i]
        helper(nums, ind+1, res)
        nums[i], nums[ind] = nums[ind], nums[i]
    }
}

func permute(nums []int) [][]int {
    var res [][]int
    helper(nums, 0, &res)
    return res
}

"""
// Python Code
class Solution:
    def helper(self, nums, ind, res):
        if ind == len(nums):
            res.append(nums.copy())
            return
        for i in range(ind, len(nums)):
            nums[i], nums[ind] = nums[ind], nums[i]
            self.helper(nums, ind+1, res)
            nums[i], nums[ind] = nums[ind], nums[i]



    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        self.helper(nums, 0, res)
        return res
"""