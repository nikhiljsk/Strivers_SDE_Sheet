// Approach 1
// Naive Approach - For each i, check if i+j == target
// O(N2), O(1)
func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{j, i}
			}
		}
	}
	return []int{}
}

// Approach 2
// Sort the array, use two pointers, start and end.
// O(N * LogN), O(1)

// Approach 3
// O(N), O(N)
func twoSum(nums []int, target int) []int {
	find := make(map[int]int)
	for i, v := range nums {
		if j, ok := find[v]; ok && i != j {
			return []int{j, i}
		}
		find[target-v] = i
	}
	return []int{}
}

// Follow-up question - GFG
// If two unsorted arrays are given, and to find a pair
// Also given: All pairs should be printed in increasing order of u.
// For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
// (u1,v1) should be printed first else second.
// Hence Sorting needs to be done
// O(N * LogN), O(N)
func allPairs(A, B []int, N, M, X int) [][]int {
	found := make(map[int]int)
	var res [][]int
	sort.Ints(A[:])
	for i := 0; i < len(B); i++ {
		found[B[i]] = i
	}
	for i := 0; i < len(A); i++ {
		if _, ok := found[X-A[i]]; ok {
			res = append(res, []int{A[i], B[found[X-A[i]]]})
		}
	}
	return res
}