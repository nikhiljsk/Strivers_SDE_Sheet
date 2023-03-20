// Approach 1 - TLE!
// Brute Force
// O(N2), O(1)
func max(a, b int) int {
	if a >= b {
		return a
	}
	return b
}

func maxSubArray(nums []int) int {
	maxSum := nums[0]
	for i := 0; i < len(nums); i++ {
		tempSum := 0
		for j := i; j < len(nums); j++ {
			tempSum += nums[j]
			maxSum = max(maxSum, tempSum)
		}
	}
	return maxSum
}

// Approach 2 - Optimized
// Kadane's Algorithm
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

// Follow-up question
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

// Similar - But not sure if it works for all - But is more intuitive
func maxSubArray(nums []int) int {
	localMax, globalMax := -2147483648, -2147483648
	start := 0
	var res [2]int
	for i, v := range nums {
		if v > localMax+v {
			localMax = v
			start = i
		} else {
			localMax += v
		}
		if globalMax < localMax {
			globalMax = localMax
			// Store the result
			res[0] = start
			res[1] = i
		}
	}
	fmt.Println(res[0], res[1])
	return globalMax
}

"""
// Python Solution - Consider this the final Solution tha works perfectly
class Solution:
    def maxSubArraySum(self, nums, N):
    	localMax, globalMax = -2147483648, -2147483648
    	start = 0
    	res = [0, 0]
    	for i in range(len(nums)):
    	    v = nums[i]
    		if v > localMax+v:
    			localMax = v
    			start = i
    		else:
    			localMax += v

    		if globalMax < localMax:
    			globalMax = localMax
    			res[0] = start
    			res[1] = i
    	# print(res[0], res[1])
    	return globalMax
"""

// Approach - Yes
// Implementation - No - max(local, local+i), here it should be (i, local+i)