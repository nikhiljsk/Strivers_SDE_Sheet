// Approach 1
// O(N2), O(1) - Two Passes
func rotate(matrix [][]int) {
	// Transpose
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < i; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	// Reverse the rows
	n := len(matrix)
	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0])/2; j++ {
			matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
		}
	}
}

// Approach 2
// O(N2), O(1) - One pass
// Spiral replace
// Refer this to understand this: https://dev.to/seanpgallivan/solution-rotate-image-cpp
func rotate(matrix [][]int) {
	n := len(matrix)
	depth := n / 2 // Since for each ring shortens by 2
	t, b, l, r := 0, n-1, 0, n-1
	for i := 0; i < depth; i++ {
		jLen := n - (2 * i) - 1 // Since far right side are already swapped
		for j := 0; j < jLen; j++ {
			temp := matrix[t][l+j]
			matrix[t][l+j] = matrix[b-j][l]
			matrix[b-j][l] = matrix[b][r-j]
			matrix[b][r-j] = matrix[t+j][r]
			matrix[t+j][r] = temp
		}
		r--
		l++
		b--
		t++
	}
}