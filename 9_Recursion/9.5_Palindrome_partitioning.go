// Approach 1
// Decide in each place if a partition can be made. Partition is made if it is a palindrome
// O(2**N) * N, O(N * N)
func helper(s string, ind int, path []string, res *[][]string) {
	if ind == len(s) {
		tmp := make([]string, len(path))
		copy(tmp, path)
		*res = append(*res, tmp)
		return
	}
	for i := ind; i < len(s); i++ {
		if isPal(s, ind, i) {
			path = append(path, s[ind:i+1])
			helper(s, i+1, path, res)
			path = path[:len(path)-1]
		}
	}
}

func partition(s string) [][]string {
	res := make([][]string, 0)
	path := make([]string, 0)
	helper(s, 0, path, &res)
	return res
}

func isPal(s string, start, end int) bool {
	for start < end {
		if s[start] != s[end] {
			return false
		}
		start++
		end--
	}
	return true
}