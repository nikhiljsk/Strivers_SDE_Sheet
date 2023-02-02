# Approach 1
# Brute force
# O(N2), O(1)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = list()
        for i in range(n):
            j = i+1
            while j%n != i:
                j = j%n
                if nums[i] < nums[j]:
                    res.append(nums[j])
                    break
                j+=1
            if j%n == i:
                res.append(-1)
        return res
            

# Approach 2
# Using Stack
# O(N), O(N)
from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        n = len(nums)
        res = [-1] * n

        i = 2*n-1
        while i>=0:
            while len(stack) != 0 and stack[-1] <= nums[i%n]:
                stack.pop()
            
            if i < n:
                if len(stack) != 0:
                    res[i] = stack[-1]
                
            stack.append(nums[i%n])
            i-=1

        return res