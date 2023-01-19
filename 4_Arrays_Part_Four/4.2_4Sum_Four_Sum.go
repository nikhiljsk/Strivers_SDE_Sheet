// Approach 3
// O(N3), O(1)
func fourSum(nums []int, target int) [][]int {
	res := make([][]int, 0)
	sort.Ints(nums)
	n := len(nums)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			// Now do a 2Sum using two pointers on sorted array
			target2 := target - nums[i] - nums[j]
			l, r := j+1, n-1
			for l < r {
				curr := nums[l] + nums[r]
				if curr == target2 {
					res = append(res, []int{nums[i], nums[j], nums[l], nums[r]})

					// Skip duplicates for 3rd pointer (Left)
					for (l < r) && (nums[l+1] == nums[l]) {
						l++
					}

					// Skip duplicates for 4th pointer (Right)
					for (l < r) && (nums[r-1] == nums[r]) {
						r--
					}
					l++
					r--

				} else if curr < target2 {
					l++
				} else {
					r--
				}
			}
			// Skip duplicates for 2nd pointer (j)
			for j < (n-1) && (nums[j+1] == nums[j]) {
				j++
			}
		}
		// Skip duplicates for 1st pointe (i)
		for i < (n-1) && (nums[i+1] == nums[i]) {
			i++
		}
	}
	return res
}