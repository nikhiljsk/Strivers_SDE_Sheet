# Approach 1
# O(N2), O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            l, r = i, i
            while l>=0 and heights[l] >= heights[i]:
                l-=1
            while r<n and heights[r] >= heights[i]:
                r+=1
            res = max(res, (r-l-1)*heights[i])
        return res

# Approach 2
# O(3N), O(3N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # To the left
        stack = list()
        nsl = [0]*n
        for i in range(n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) != 0:
                nsl[i] = stack[-1] + 1
            stack.append(i)

        # To the right
        stack = list()
        nsr = [n-1]*n
        for i in range(n-1, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) != 0:
                nsr[i] = stack[-1] - 1
            stack.append(i)

        # Calculate
        res = heights[0]
        for i in range(n):
            weidth = nsr[i] - nsl[i] + 1
            res = max(res, heights[i] * weidth)

        return res

# Approach 3
# O(2N), O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        maxArea = 0
        n = len(heights)
        for i in range(n+1):
            while (len(stack)!=0 and (i==n or heights[stack[-1]] >= heights[i])):
                height = heights[stack.pop()]
                if len(stack) == 0:
                    width = i
                else:
                    width = i-stack[-1]-1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
