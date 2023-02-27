// Approach 1 - Naive Approach
// O(M*N), O(1)
// TLE!

// Approach 2 - Navigate intelligently
// O(M+N), O(1)
func searchMatrix(matrix [][]int, target int) bool {
	nRows, nCols := len(matrix), len(matrix[0])
	i, j := 0, nCols-1
	for i < nRows && j >= 0 {
		curr := matrix[i][j]
		if target < curr {
			j -= 1
		} else if target > curr {
			i += 1
		} else {
			return true
		}
	}
	return false
}

// Approach 2 - Treat as 1D Array
// O(log(M*N)), O(1)
func searchMatrix(arr [][]int, target int) bool {
	l, r, c := 0, len(arr)*len(arr[0])-1, len(arr[0])
	for l <= r {
		mid := l + ((r - l) / 2)
		if arr[mid/c][mid%c] == target {
			return true
		}
		if arr[mid/c][mid%c] > target {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return false
}