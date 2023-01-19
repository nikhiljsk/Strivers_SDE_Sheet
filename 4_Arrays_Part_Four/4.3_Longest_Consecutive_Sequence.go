// Approach 1
// Sort the array, skip duplicates, count consecutives
// O(N * LogN), O(1)
func longestConsecutive(nums []int) int {
	if len(nums) == 0 || len(nums) == 1 {
		return len(nums)
	}
	sort.Ints(nums)
	prev := nums[0]
	res, count := 1, 1
	for i := 1; i < len(nums); i++ {
		if prev+1 == nums[i] {
			count++
			if count > res {
				res = count
			}
		} else {
			count = 1
		}
		prev = nums[i]
		// Skip duplicates
		for (i < len(nums)-1) && (nums[i] == nums[i+1]) {
			i++
		}
	}
	return res
}

// Approach 2
// Intution here is you won't keep finding the if the same sequence exists over and over. Just do it once with
// the minimum element possible so as keep complexity low
// O(3N), O(N)
func longestConsecutive(nums []int) int {
	found := make(map[int]bool)
	for _, v := range nums {
		found[v] = true
	}

	res := 0

	for k, _ := range found {
		// Allow next for loop, only if not part of sequences found so far
		// Also don't allow any number which has a previous number
		if _, ok := found[k-1]; !ok {
			_, isExists := found[k+1]
			count := 1
			curr := k + 1
			for isExists {
				count++
				curr++
				_, isExists = found[curr]
			}
			if res < count {
				res = count
			}
		}
	}
	return res
}