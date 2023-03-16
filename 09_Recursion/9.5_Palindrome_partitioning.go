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


"""
// Python Code
class Solution:
    def isPal(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start+=1
            end-=1
        return True


    def helper(self, s, ind, ds, res):
        if ind == len(s):
            res.append(ds.copy())
            return

        for i in range(ind, len(s)):
            if self.isPal(s, ind, i):
                ds.append(s[ind:i+1])
                self.helper(s, i+1, ds, res)
                ds.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = list()
        self.helper(s, 0, [], res)
        return res
"""