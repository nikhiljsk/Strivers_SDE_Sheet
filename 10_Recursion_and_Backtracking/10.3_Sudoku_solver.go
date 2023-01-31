// Approach 1
// O(9 ^ (n ^ 2)), O(1)
func isValidSudoku(board [][]byte, row, col int, num byte) bool {
	for i := 0; i < len(board); i++ {
		if board[i][col] == num {
			return false
		}
		if board[row][i] == num {
			return false
		}
		if board[3*(row/3)+i/3][3*(col/3)+i%3] == num {
			return false
		}
	}
	return true
}

func helper(board [][]byte) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board); j++ {
			if board[i][j] != '.' {
				continue
			}

			for k := '1'; k <= '9'; k++ {
				if isValidSudoku(board, i, j, byte(k)) {
					board[i][j] = byte(k)
					if helper(board) == true {
						return true
					} else {
						board[i][j] = '.'
					}
				}
			}
			return false
		}
	}
	return true
}

func solveSudoku(board [][]byte) {
	helper(board)
}