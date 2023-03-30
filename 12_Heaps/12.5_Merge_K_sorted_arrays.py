# Approach 1
# Using Heaps
# O(NLogN), O(N)
from heapq import heappush, heappop

def mergeKSortedArrays(kArrays, k:int):
	heap = list()
	for arr in kArrays:
		for i in arr:
			heappush(heap, i)

	res = list()
	while heap:
		res.append(heappop(heap))
	return res