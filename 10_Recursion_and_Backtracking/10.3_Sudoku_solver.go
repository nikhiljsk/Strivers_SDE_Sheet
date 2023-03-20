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

"""
// Python Code
class Solution:
    def isValid(self, board, row, col, num):
        for i in range(len(board)):
            if board[i][col] == num:
                return False
            if board[row][i] == num:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == num:
                return False
        return True


    def helper(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    continue

                for k in range(1, 10):
                    if self.isValid(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if self.helper(board):
                            return True
                        else:
                            board[i][j] = "."
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.helper(board)
"""