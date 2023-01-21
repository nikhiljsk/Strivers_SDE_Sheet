// Appraoch 1 - Brute Force
// O(N2), O(1)
func solve(arr []int, B int) int {
	count := 0
	for i := 0; i < len(arr); i++ {
		xor := 0
		for j := i; j < len(arr); j++ {
			xor ^= arr[j]
			if xor == B {
				count++
			}
		}
	}
	return count
}

// Approach 2
// O(N), O(N)
// The approach here is to store prefix_xor and count of how many times you've seen it.
// Then do Y = XR ^ K, to find out the number of arrays contributing so far to given target
func solve(arr []int, target int) int {
	prefix_xor := make(map[int]int)
	curr_xor, count := 0, 0
	for i := 0; i < len(arr); i++ {
		curr_xor ^= arr[i]
		if curr_xor == target {
			count++
		}

		y := curr_xor ^ target // Y = XR ^ K
		if _, ok := prefix_xor[y]; ok {
			count += prefix_xor[y]
		}

		if _, ok := prefix_xor[curr_xor]; ok {
			prefix_xor[curr_xor] += 1
		} else {
			prefix_xor[curr_xor] = 1
		}
	}
	return count
}