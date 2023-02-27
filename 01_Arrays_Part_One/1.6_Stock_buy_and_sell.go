// Approach 1
// TLE!
// O(N2), O(1)
func maxProfit(prices []int) int {
	var res int
	for i := 0; i < len(prices)-1; i++ {
		for j := i + 1; j < len(prices); j++ {
			temp := prices[j] - prices[i]
			if temp > res {
				res = temp
			}
		}
	}
	return res
}

// Approach 2
// Store the min element found so far in the left side.
// O(N), O(1)
func maxProfit(prices []int) int {
	var res int
	min := 2147483647
	for i := 0; i < len(prices); i++ {
		if prices[i] < min {
			min = prices[i]
		}
		temp := prices[i] - min
		if temp > res {
			res = temp
		}
	}
	return res
}