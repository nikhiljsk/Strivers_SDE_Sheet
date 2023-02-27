package main

import (
	"fmt"
	"sort"
)

// Approach 1
// O(N * LogN), O(1)
// Sort and find any duplicate
func findDuplicate3(nums []int) int {
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			return nums[i]
		}
	}
	return 0
}

// Approach 2
// O(N), O(1) - Array is modified
// Jump to index mentioned in value, negate it. If already negation found, that means duplicate
func abs(a int) int {
	if a < 0 {
		return -1 * a
	}
	return a
}
func findDuplicate2(nums []int) int {
	for _, v := range nums {
		cur := abs(v)
		if nums[cur] < 0 {
			return cur
		}
		nums[cur] = -1 * nums[cur]
	}
	return 0
}

// Approach 3
// O(N), O(1) - Array is NOT modified
// Floyd's Cycle - Tortoise and Hare approach
// Tip - It is essential for t and h to start at same point to find the start point of cycle.
func findDuplicate(nums []int) int {
	t, h := nums[0], nums[0]
	for {
		t = nums[t]
		h = nums[nums[h]]
		if t == h {
			break
		}
	}
	// First intersection point found - indicates cycle exists
	// Now, find cycle start point, by incrementing one
	t = nums[0]
	for t != h {
		t = nums[t]
		h = nums[h]
	}
	return t
}

func main() {
	arr := []int{1, 3, 4, 2, 2}
	fmt.Println(findDuplicate(arr))
}
