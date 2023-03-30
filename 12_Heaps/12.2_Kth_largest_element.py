# Approach 1
# Sort and return
# O(NLogN), O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]


# Approach 2
# Insert negative numbers in minHeap to convert it to Max heap
# O(N + klogN), O(n)
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)

        for i in range(k-1):
            heapq.heappop(max_heap)
        return -max_heap[0]


# Approach 3
# Max heap in python
# O(nlogn + klogk), O(1)
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)

        for i in range(k-1):
            heapq._heappop_max(nums)
        return nums[0]


# Approach 4
# Quick Select Partition Algo
# O(N) Avg. Case, O(N2) Worst Case, O(1)
class Solution:
    def quickSelect(self, nums, l, r, k):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return self.quickSelect(nums, l, p-1, k)
        elif p < k:
            return self.quickSelect(nums, p+1, r, k)
        else:
            return nums[p]



    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        return self.quickSelect(nums, 0, len(nums)-1, k)
