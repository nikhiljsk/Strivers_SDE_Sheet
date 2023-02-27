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
// O(N2), O(N2) - If we calculate storage for output
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

// Other follow-up questions in Pascal's
// Follow-up question 1
// Return a particular value in the row.
// That is calclated by binomial coefficient.
// If row-C-col; so if 3rd value in 4th row: 4C3
// where n=4, k=3
// For more info: https://www.youtube.com/watch?v=6FLvhQjZqvM&list=PLgUwDviBIf0rPG3Ictpu74YWBQ1CaBkm2&index=9&ab_channel=takeUforward
// O(N), O(1)
res = 1
for i:=0; i<k; i++{
	res *= (n-i)
	res /= (i+1)
}

// Follow-up question 2
// Return a particular row
// Similar to the above, just return using the binomial coefficient.
// O(N), O(N) - If we calculate storage for output