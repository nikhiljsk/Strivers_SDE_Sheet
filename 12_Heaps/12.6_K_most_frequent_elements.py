# Approach 1
# Python In-built functions
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, _ in collections.Counter(nums).most_common(k)]


# Approach 2
# Using Heap
# O(NLogK), O(N)
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency dict
        found = defaultdict(int)
        for n in nums:
            found[n] += 1

        # Create Heap and maintain only k elements in heap
        heap = list()
        for key in found:
            heapq.heappush(heap, (found[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        # Pop and copy the answer
        res = list()
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res


# Approach 3
# Inverse mapping of val, freq to freq, val. Then iterating from n to 1
# O(N), O(N)
from collections import defaultdict, Counter
class Solution:
    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        found, res = Counter(nums), []
        inv_frequency = defaultdict(list)

        # Frequency to item mapping
        for key, freq in found.items():
            inv_frequency[freq].append(key)

		# Populate Result
        for i in range(len(nums), 0, -1):
            res.extend(inv_frequency[i])
            if len(res) >= k:
                break
        return res[:k]