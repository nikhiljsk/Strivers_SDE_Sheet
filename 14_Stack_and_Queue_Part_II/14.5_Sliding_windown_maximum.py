# Approach 1 - TLE!
# O(N*K), O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = list()
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res


# Approach 2 - Deque - Accepted
# O(2N), O(K)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans = list()
        for i in range(len(nums)):
            # Remove the element that is out of the current search range
            if len(dq) != 0 and dq[0] <= (i-k):
                dq.popleft()

            # Remove all the elements from the back if smaller than current to maintain decreasing order
            while len(dq)!=0 and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Push the current element
            dq.append(i)

            # Store the answer
            if i >= k-1:
                ans.append(nums[dq[0]])
        return ans
