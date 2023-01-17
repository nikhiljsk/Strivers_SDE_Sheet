// Approach 1 - Naive Solution - TLE!
// O(N), O(1)
// You also have to handle the edge case - Where int_min conversion to absolute will overflowc
func abs(a int) int {
	if a > 0 {
		return a
	}
	return -1 * a
}

func myPow(x float64, n int) float64 {
	if n == 0 {
		return 1
	}
	res, N := x, abs(n)
	for i := 1; i < N; i++ {
		res *= x
	}
	if n > 0 {
		return res
	}
	return 1 / res
}

// Approach 2
// O(LogN), O(1)
func abs(a int) int {
	if a > 0 {
		return a
	}
	return -1 * a
}

func myPow(x float64, n int) float64 {
	res, N := 1.0, abs(n)
	for N > 0 {
		if N%2 == 0 {
			x *= x
			N /= 2
		} else {
			res *= x
			N -= 1
		}
	}
	if n > 0 {
		return res
	}
	return 1 / res
}