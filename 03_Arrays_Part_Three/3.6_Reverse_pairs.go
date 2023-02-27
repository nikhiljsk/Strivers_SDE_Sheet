// Approach 1 - TLE!
// O(N2), O(1)
func reversePairs(nums []int) int {
	c := 0
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > 2*nums[j] {
				c++
			}
		}
	}
	return c
}

// Approach 2
// Merge Sort approach
// O(N * LogN), O(N)
func merge(arr []int, left, mid, right int) int {
	reverse_count := 0
	i, j := left, mid+1
	// The intuition here for counting before starting the merge, unlike array inversions:
	// It is not necessary that if arr[i] > arr[j], the subsequent i+1... will be 2 times greater than j+1
	// For inversion count, the above condition does not contain 2 times greater than, hence it is satisied.
	for i <= mid {
		for j <= right && arr[i] > (2*arr[j]) {
			j++
		}
		reverse_count += (j - (mid + 1))
		i++
	}

	i, j, k := left, mid+1, left
	temp := make([]int, right+1)
	for i <= mid && j <= right {
		if arr[i] <= arr[j] {
			temp[k] = arr[i]
			i++
		} else {
			temp[k] = arr[j]
			j++
		}
		k++
	}

	for i <= mid {
		temp[k] = arr[i]
		i++
		k++
	}

	for j <= right {
		temp[k] = arr[j]
		j++
		k++
	}

	for i = left; i <= right; i++ {
		arr[i] = temp[i]
	}
	return reverse_count
}

func mergeSort(arr []int, left, right int) int {
	reverse_count := 0
	if left < right {
		mid := (left + right) / 2
		reverse_count += mergeSort(arr, left, mid)
		reverse_count += mergeSort(arr, mid+1, right)
		reverse_count += merge(arr, left, mid, right)
	}
	return reverse_count
}

func reversePairs(nums []int) int {
	return mergeSort(nums, 0, len(nums)-1)
}