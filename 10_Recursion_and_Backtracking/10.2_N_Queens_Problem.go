// Approach 1
// O(N!), O(N2)
func isSafe(board []string, row, col, n int) bool {
	// Check upper left diagnol
	dRow, dCol := row, col
	for row >= 0 && col >= 0 {
		if board[row][col] == []byte("Q")[0] {
			return false
		}
		row--
		col--
	}

	// Check left
	row, col = dRow, dCol
	for col >= 0 {
		if board[row][col] == []byte("Q")[0] {
			return false
		}
		col--
	}

	// Check lower left diagnol
	row, col = dRow, dCol
	for row < n && col >= 0 {
		if board[row][col] == []byte("Q")[0] {
			return false
		}
		row++
		col--
	}
	return true
}

func helper(col int, board []string, ans *[][]string, n int) {
	if col == n {
		tmp := make([]string, len(board))
		copy(tmp, board)
		*ans = append(*ans, tmp)
		return
	}
	for row := 0; row < n; row++ {
		if isSafe(board, row, col, n) {
			v := []byte(board[row])
			v[col] = []byte("Q")[0]
			board[row] = string(v)

			helper(col+1, board, ans, n)

			v = []byte(board[row])
			v[col] = []byte(".")[0]
			board[row] = string(v)
		}
	}
}

func solveNQueens(n int) [][]string {
	var board []string
	for i := 0; i < n; i++ {
		tmp := ""
		for j := 0; j < n; j++ {
			tmp += "."
		}
		board = append(board, tmp)
	}
	var ans [][]string
	helper(0, board, &ans, n)
	return ans
}

// Approach 2
// A cleaner approach than above
func helper(col int, board []string, ans *[][]string, leftRow, upperDiag, lowerDiag []int, n int) {
	if col == n {
		tmp := make([]string, len(board))
		copy(tmp, board)
		*ans = append(*ans, tmp)
		return
	}
	for row := 0; row < n; row++ {
		if leftRow[row] == 0 && lowerDiag[row+col] == 0 && upperDiag[n-1+col-row] == 0 {
			v := []byte(board[row])
			v[col] = []byte("Q")[0]
			board[row] = string(v)

			leftRow[row] = 1
			lowerDiag[row+col] = 1
			upperDiag[n-1+col-row] = 1

			helper(col+1, board, ans, leftRow, upperDiag, lowerDiag, n)

			leftRow[row] = 0
			lowerDiag[row+col] = 0
			upperDiag[n-1+col-row] = 0

			v = []byte(board[row])
			v[col] = []byte(".")[0]
			board[row] = string(v)
		}
	}
}

func solveNQueens(n int) [][]string {
	var board []string
	for i := 0; i < n; i++ {
		tmp := ""
		for j := 0; j < n; j++ {
			tmp += "."
		}
		board = append(board, tmp)
	}
	var ans [][]string
	leftRow := make([]int, n)
	upperDiag := make([]int, 2*n-1)
	lowerDiag := make([]int, 2*n-1)
	helper(0, board, &ans, leftRow, upperDiag, lowerDiag, n)
	return ans
}