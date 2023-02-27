func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// O(N * logN), O(N) - If output storage is considered
func merge(intervals [][]int) [][]int {
	// Sort the array based on 0th column element
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][0] < intervals[j][0] {
			return true
		}
		return false
	})

	res := make([][]int, 0)
	left, right := intervals[0][0], intervals[0][1]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] <= right {
			right = max(right, intervals[i][1])
		} else {
			res = append(res, []int{left, right})
			left, right = intervals[i][0], intervals[i][1]
		}
	}
	res = append(res, []int{left, right})
	return res
}