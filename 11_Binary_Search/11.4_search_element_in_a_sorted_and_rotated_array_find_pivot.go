package main

import "fmt"

// Approach 1
// O(N), O(1)
// Linear Search

// Approach 2
// Finding the Pivot and then do Binary search on both the parts
// O(LogN), O(1) - But multiple passes
func findPivot(arr []int, l, r int) int {
	last := arr[r]
	for l <= r {
		mid := l + (r-l)/2
		if arr[mid] > last {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return l
}

func bSearch(arr []int, target int) (bool, int) {
	l, r := 0, len(arr)-1
	for l <= r {
		mid := l + (r-l)/2
		if arr[mid] == target {
			return true, mid
		}
		if arr[mid] < target {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return false, -1
}

func search(nums []int, target int) int {
	pivot := findPivot(nums, 0, len(nums)-1)
	found, ind := bSearch(nums[:pivot], target)
	if found {
		return ind
	}
	found, ind = bSearch(nums[pivot:], target)
	if found {
		return pivot + ind
	}
	return -1
}

// Approach 3 - Optimal
// O(LogN), O(1)
func search2(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		mid := l + (r-l)/2
		if nums[mid] == target {
			return mid
		}

		// If left half is sorted
		if nums[l] <= nums[mid] {
			if nums[l] <= target && target <= nums[mid] { // Inside left half, check where to move
				r = mid - 1
			} else {
				l = mid + 1
			}

		} else { // If right half is sorted
			if nums[mid] <= target && target <= nums[r] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		}
	}
	return -1
}

// Follow-up question
// What if the elements are not distinct
func search3(nums []int, target int) bool {
	l, r := 0, len(nums)-1
	for l <= r {
		mid := l + (r-l)/2
		if nums[mid] == target {
			return true
		}

		// The only case where you might find problem, is when arr[l]==arr[mid]==arr[r]
		// So you'll have to reduce the search space in this case
		// This will be the only difference from sorted array search I
		if nums[l] == nums[mid] && nums[mid] == nums[r] {
			l++
			r--
			continue
		}

		// If left half is sorted
		if nums[l] <= nums[mid] {
			if nums[l] <= target && target <= nums[mid] {
				r = mid - 1
			} else {
				l = mid + 1
			}

		} else {
			if nums[mid] <= target && target <= nums[r] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		}
	}
	return false
}

func main() {
	arr := []int{3, 3, 4, 5, 1, 2, 3}
	arr = []int{1, 0, 1, 1, 1}
	target := 0
	fmt.Println(search3(arr, target))

}
