// Approach 1
// Own
// O(N2), O(N2) - If we calculate storage for output
func generate(numRows int) [][]int {
	res := make([][]int, 0)
	res = append(res, []int{1})
	for i := 2; i <= numRows; i++ {
		res = append(res, genNext(res[len(res)-1], i))
	}
	return res
}

func genNext(arr []int, n int) []int {
	res := make([]int, len(arr)+1)
	res[0] = 1
	var i int
	for i = 1; i < n-1; i++ {
		res[i] = arr[i-1] + arr[i]
	}
	res[len(arr)] = 1
	return res
}

// Approach 2
// Solution
func generate(n int) [][]int {
	res := make([][]int, 0)

	for i := 0; i < n; i++ {
		res = append(res, make([]int, i+1))
		res[i][0] = 1
		res[i][i] = 1

		for j := 1; j < i; j++ {
			res[i][j] = res[i-1][j-1] + res[i-1][j]
		}
	}
	return res
}

// Approach - Yes
// Implementation - Yes