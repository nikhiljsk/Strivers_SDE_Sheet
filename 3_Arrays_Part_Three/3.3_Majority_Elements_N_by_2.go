// Approach 1
// Sort the array, return arr[mid+1]
// O(N * LogN), O(1)
func majorityElement(nums []int) int {
	sort.Ints(nums[:])
	return nums[len(nums)/2]
}

// Approach 2
// Count the freq in hashmap
// O(N), O(N)

// Approach 3
// Moore's voting algorithm
// Works only for greater than n/2, if >= condition is given this won't work. As the other elements cancel this out.
// O(N), O(1)
func majorityElement(arr []int) int {
	curr, curr_freq := arr[0], 1

	for i := 1; i < len(arr); i++ {
		if arr[i] == curr {
			curr_freq++
		} else {
			curr_freq--
		}
		if curr_freq < 0 {
			curr = arr[i]
			curr_freq = 1
		}
	}

	return curr
}