// Similar to kth element in two sorted arrays
// https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=k-th-element-of-two-sorted-array

// Approach 1
// Copy both the arrays into new arrays, then sort the entire array, return mid
// O(NLogN), O(N)

// Approach 2
// Using two pointer approach to create new merged sorted array, then return mid
// O(N), O(N)

// Approach 3
// Similar to above approach, but just have a count, so as to not store the elements
// O(N), O(1)

// Approach 4
// Binary Search - O(LogN), O(1)
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	if len(nums2) < len(nums1) { // This is necessary here. Take the case [2], []. Then cut1 will be 0, but cut2 will be 1. Invalid
		return findMedianSortedArrays(nums2, nums1)
	}
	n1, n2 := len(nums1), len(nums2)
	low, high := 0, n1
	int_min, int_max := -2147483648, 2147483647

	for low <= high {
		cut1 := (low + high) >> 1
		cut2 := (n1+n2+1)/2 - cut1

		var l1, l2, r1, r2 int
		if cut1 == 0 {
			l1 = int_min
		} else {
			l1 = nums1[cut1-1]
		}
		if cut2 == 0 {
			l2 = int_min
		} else {
			l2 = nums2[cut2-1]
		}
		if cut1 == n1 {
			r1 = int_max
		} else {
			r1 = nums1[cut1]
		}
		if cut2 == n2 {
			r2 = int_max
		} else {
			r2 = nums2[cut2]
		}

		if (l1 <= r2) && (l2 <= r1) {
			if (n1+n2)%2 == 0 {
				return float64(max(l1, l2)+min(r1, r2)) / 2
			}
			return float64(max(l1, l2))
		} else if l1 > r2 {
			high = cut1 - 1
		} else {
			low = cut1 + 1
		}
	}
	return 0.0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}