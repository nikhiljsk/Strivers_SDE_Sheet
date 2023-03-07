// Approach 1 - TLE!
// Brute Force
// O(n3), O(3^k) where k is number of triplets - If Solution space is considered
func threeSum(nums []int) [][]int {
	res := make([][]int, 0)
	n := len(nums)
	found := make(map[triplet]bool) // You can't have []int as keys in map, hence triplet
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				if nums[i]+nums[j]+nums[k] == 0 {
					temp := [3]int{nums[i], nums[j], nums[k]}
					sort.Ints(temp[:])
					if _, ok := found[triplet{temp}]; !ok {
						res = append(res, []int{nums[i], nums[j], nums[k]})
						found[triplet{temp}] = true
					}
				}
			}
		}
	}
	return res
}

// Python Code - TLE!
// Using a tuple which is inserted in set for de-duplication
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, res, found = len(nums), list(), set()

        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a+b+c == 0:
                        triplet = tuple(sorted([a, b, c]))
                        if triplet not in found:
                            found.add(triplet)
                            res.append(list(triplet))

        return res
"""

// Approach 2
// O(N2), O(3^k)
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	var res [][]int
	for i := 0; i < len(nums); i++ {
		target := 0 - nums[i]
		l, r := i+1, len(nums)-1
		for l < r {
			sum := nums[l] + nums[r]
			if sum == target {
				res = append(res, []int{nums[i], nums[l], nums[r]})

				// Skip duplicates for l
				for l < r && nums[l] == nums[l+1] {
					l++
				}
				// Skip duplicates for r
				for l < r && nums[r] == nums[r-1] {
					r--
				}
				l++
				r--
			} else if sum > target {
				r--
			} else {
				l++
			}
		}
		// Skip duplicates for i
		for i < len(nums)-1 && nums[i+1] == nums[i] {
			i++
		}
	}
	return res
}