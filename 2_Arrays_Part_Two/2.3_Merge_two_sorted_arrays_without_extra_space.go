// Approach 1
// LeetCode Question
// O(N), O(1)
func merge(nums1 []int, m int, nums2 []int, n int) {
	p1, p2, k := m-1, n-1, len(nums1)-1
	for p1 >= 0 && p2 >= 0 {
		if nums1[p1] > nums2[p2] {
			nums1[k] = nums1[p1]
			p1--
		} else {
			nums1[k] = nums2[p2]
			p2--
		}
		k--
	}
	for p2 >= 0 {
		nums1[k] = nums2[p2]
		p2--
		k--
	}
}

// Approach 1
// GFG Question - TLE!
// Link: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
// O(N2)
def merge(self,arr1,arr2,n,m):
	for i in range(n):
		if arr1[i] > arr2[0]:
			arr1[i], arr2[0] = arr2[0], arr1[i]

			// Selection sort, find the right place for arr2[0] in arr2
			first = arr2[0]
			j = 1
			while j<m and first > arr2[j]:
				arr2[j-1] = arr2[j]
				j+=1
			arr2[j-1] = first


// Approach 2
// GFG Question
// O(N * logN), O(1)
def merge(self,arr1,arr2,n,m):
	gap = math.ceil((n+m)//2)

	while gap > 0:
		i, j = 0, gap
		while j < n+m:
			if i < n and j >= n and arr1[i] > arr2[j-n]: # If one in arr1 other in arr2
				arr1[i], arr2[j-n] = arr2[j-n], arr1[i]
			elif i>=n and j>=n and arr2[i-n] > arr2[j-n]: # If both pointers in same arr2
				arr2[i-n], arr2[j-n] = arr2[j-n], arr2[i-n]
			elif i<n and j<n and arr1[i] > arr1[j]: # If both pointers in same arr1
				arr1[i], arr1[j] = arr1[j], arr1[i]
			i+=1
			j+=1

		if gap == 1:
			break
		gap = math.ceil(gap/2)