// Approach 1
// O(NLogN), O(1)
func books(arr []int, k int) int {
	if k > len(arr) {
		return -1
	}
	low, high := arr[0], 0
	for _, v := range arr {
		high += v
		if v < low {
			low = v
		}
	}

	for low <= high {
		mid := (low + high) >> 1
		if isPossible(arr, mid, k) {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return low
}

func isPossible(arr []int, mid, k int) bool {
	count, pages := 1, 0
	for _, v := range arr {
		if v > mid {
			return false
		}
		if pages+v > mid {
			pages = v
			count++
		} else {
			pages += v
		}
	}
	if count <= k {
		return true
	}
	return false
}