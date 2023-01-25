// Approach 1
// For each i, find the left max and right max and do accordingly
// O(N2), O(1)

// Approach 2
// Calculate prefix sum array and suffix sum array
// O(2N), O(2N)
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func trap(height []int) int {
	n := len(height)
	preSum, sufSum := make([]int, n), make([]int, n)
	i, j := height[0], height[n-1]
	for k := 0; k < n; k++ {
		if i < height[k] {
			i = height[k]
		}
		if j < height[n-k-1] {
			j = height[n-k-1]
		}
		preSum[k] = i
		sufSum[n-k-1] = j
	}

	water := 0
	for i = 0; i < n; i++ {
		// Max here is redundant, not necessary as max height is stored starting from that point
		water += max(0, min(preSum[i], sufSum[i])-height[i])
	}
	return water
}

// Approach 3
// Similar to the above, but use two pointers instead
// O(N), O(1)
func trap(height []int) int {
	l, r := 0, len(height)-1
	res, lMax, rMax := 0, 0, 0
	for l <= r {
		if height[l] <= height[r] {
			if height[l] > lMax {
				lMax = height[l]
			} else {
				res += (lMax - height[l])
			}
			l++
		} else {
			if height[r] > rMax {
				rMax = height[r]
			} else {
				res += (rMax - height[r])
			}
			r--
		}
	}
	return res
}