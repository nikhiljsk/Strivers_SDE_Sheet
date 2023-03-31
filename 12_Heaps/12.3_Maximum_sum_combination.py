# Approach 1 - TLE!
# O(N2), O(N2)
import heapq

class Solution:
    def solve(self, A, B, C):
        i, j = 0, 0
        min_heap = list()
        for i in range(len(A)):
            for j in range(len(B)):
                heapq.heappush(min_heap, -1 * (A[i]+A[j]))

        res = list()
        for i in range(C):
            res.append(-1 * heapq.heappop(min_heap))
        return res


# Approach 2
# O(NLogN), O(N)
from heapq import heappop, heappush

class Solution:
    def solve(self, A, B, C):
        A = sorted(A, reverse=True)
        B = sorted(B, reverse=True)

        heap = [(-A[0]-B[0], 0, 0)]
        visited, res = set(), list()
        visited.add((0,0))

        while len(res) < C:
            summ, ind_a, ind_b = heappop(heap)
            res.append(-summ)

            if (ind_a+1, ind_b) not in visited and ind_a+1 < len(A):
                heappush(heap, (-A[ind_a+1]-B[ind_b], ind_a+1, ind_b))
                visited.add((ind_a+1, ind_b))
            if (ind_a, ind_b+1) not in visited and ind_b+1 < len(B):
                heappush(heap, (-A[ind_a]-B[ind_b+1], ind_a, ind_b+1))
                visited.add((ind_a, ind_b+1))
        return res