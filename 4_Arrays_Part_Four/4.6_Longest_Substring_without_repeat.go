// Appraoch 1 - Brute Force
// O(N2), O(N)
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	byteS := []byte(s)
	var res, count int
	for i := 0; i < len(byteS); i++ {
		count = 0
		found := make(map[byte]bool)
		for j := i; j < len(byteS); j++ {
			if _, ok := found[byteS[j]]; ok {
				count = max(count, j-i)
				break
			}
			found[byteS[j]] = true
			count++
		}
		res = max(res, count)
	}
	return res
}

// Approach 2 - Sliding Window
// O(2N), O(1)
// Keep decrementing l, and deleting the entry in hashmap until r is not found
func lengthOfLongestSubstring(s string) int {
	l, count := 0, 0
	seen := make(map[byte]bool, len(s))

	for r := 0; r < len(s); r++ {
		_, isPresent := seen[s[r]]
		for l < r && isPresent {
			delete(seen, s[l])
			l++
			_, isPresent = seen[s[r]]
		}
		seen[s[r]] = true
		count = max(count, r-l+1)
	}
	return count
}

// Approach 3
// O(N), O(N)
// Similar to approach 2, instead of moving left pointer one by one, move it to the index directly
// Also, l = max(v+1, l) is important, if the index value in found is lesser than the range of [l, r] ignore it.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	count, l := 0, 0
	found := make(map[byte]int)
	for r := 0; r < len(s); r++ {
		if v, ok := found[s[r]]; ok {
			l = max(l, v+1) // This kind of simulates deleting the other stuff in the hashmap when jump updating left pointer
		}
		found[s[r]] = r
		count = max(count, r-l+1)
	}
	return count
}