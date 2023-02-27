// isRow, isCol are essential here, cause the first row/cols are used are flag values
// So they can be replaced
// O(N2), O(1)
func setZeroes(matrix [][]int) {
	var isRow, isCol bool
	nRows, nCols := len(matrix), len(matrix[0])
	for i := 0; i < nRows; i++ {
		if matrix[i][0] == 0 {
			isCol = true
		}
	}
	for j := 0; j < nCols; j++ {
		if matrix[0][j] == 0 {
			isRow = true
		}
	}

	// Flag the start row and col is Zero is found
	for i := 1; i < nRows; i++ {
		for j := 1; j < nCols; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	// Replace for all values if flag found
	for i := 1; i < nRows; i++ {
		for j := 1; j < nCols; j++ {
			if matrix[i][0] == 0 || matrix[0][j] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	if isRow {
		for i := 0; i < nCols; i++ {
			matrix[0][i] = 0
		}
	}
	if isCol {
		for i := 0; i < nRows; i++ {
			matrix[i][0] = 0
		}
	}
}

// Approach - Yes
// Implementation - Yes