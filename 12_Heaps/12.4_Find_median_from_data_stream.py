# Approach 1
# O(NLogN), O(1)
from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        # Max Heap
        self.small = list()
        # Min Heap
        self.large = list()
        

    def addNum(self, num: int) -> None:
        # Push into maxheap
        heappush(self.small, -1 * num)

        # If any element in small heap is greater in value than any element in large heap
        if self.small and self.large and (self.small[0] * -1) > self.large[0]:
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        # Difference in sizes
        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)
        if len(self.small) + 1 < len(self.large):
            val = heappop(self.large)
            heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()