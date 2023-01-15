// Approach 1
// O(N), O(1) - Two passes
func sortColors(nums []int) {
	found := make([]int, 3)
	for _, v := range nums {
		found[v] += 1
	}

	indx := 0
	for k, v := range found {
		i := v
		for i > 0 {
			nums[indx] = k
			indx++
			i--
		}
	}
}

// Dutch National Flag Algorithm
// O(N), O(1)
func sortColors(nums []int) {
	l, m, h := 0, 0, len(nums)-1
	for m <= h {
		switch nums[m] {
		case 0:
			nums[l], nums[m] = nums[m], nums[l]
			l++
			m++
		case 1:
			m++
		case 2:
			nums[m], nums[h] = nums[h], nums[m]
			h--
		}
	}
}