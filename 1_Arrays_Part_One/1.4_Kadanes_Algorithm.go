// Approach 1
// O(N), O(1)
func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func maxSubArray(nums []int) int {
	localMax, globalMax := -2147483648, -2147483648
	for i := 0; i < len(nums); i++ {
		localMax = max(nums[i], localMax+nums[i])
		globalMax = max(globalMax, localMax)
	}
	return globalMax
}

// Approach 2
// Approach 2
// If asked to print the subarray
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxSubArray(nums []int) int {
	localMax, globalMax := -2147483648, -2147483648
	start := 0
	var res [2]int
	for i, v := range nums {
		localMax = max(v, localMax+v)
		if globalMax < localMax {
			globalMax = localMax
			// Store the result
			res[0] = start
			res[1] = i
		}
		if localMax < 0 {
			start = i + 1
		}
	}
	fmt.Println(res[0], res[1])
	return globalMax
}

// Approach - Yes
// Implementation - No - max(local, local+i), here it should be (i, local+i)