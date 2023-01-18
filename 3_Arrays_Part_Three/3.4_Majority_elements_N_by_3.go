// Approach 1
// Count the freq in hashmap
// O(N), O(N)

// Approach 2
// Extended Moore's voting algorithm
// O(N), O(1)
func majorityElement(nums []int) []int {
	c1, c2, f1, f2 := 0, 0, 0, 0
	for _, v := range nums {
		if v == c1 {
			f1++
		} else if v == c2 {
			f2++
		} else if f1 == 0 {
			c1 = v
			f1++
		} else if f2 == 0 {
			c2 = v
			f2++
		} else {
			f1--
			f2--
		}
	}

	f1, f2 = 0, 0
	for _, v := range nums {
		if v == c1 {
			f1++
		} else if v == c2 {
			f2++
		}
	}

	var res []int
	if f1 > len(nums)/3 {
		res = append(res, c1)
	}
	if f2 > len(nums)/3 {
		res = append(res, c2)
	}
	return res
}