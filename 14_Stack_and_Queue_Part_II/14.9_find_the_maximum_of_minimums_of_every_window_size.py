# Approach 1
# Brute Force - TLE!
# O(N3), O(1)
class Solution:
    def maxOfMin(self,arr,n):
        INT_MIN = -1000000
        res = list()

        for win_size in range(1, n+1): # Consider all window sizes
            maxOfMin = INT_MIN
            for i in range(n - win_size + 1): # Iterate till n-k to consider all windows
                currMin = arr[i]  # Keep track of curr min in the window
                for j in range(win_size):  # Iterate over curr window to find currMin
                    if currMin > arr[i+j]:
                        currMin = arr[i+j]

                # Update maxOfMin
                if currMin > maxOfMin:
                    maxOfMin = currMin
            # Store the curr maxOfMin for the window
            res.append(maxOfMin)
        return res

# Approach 2
# O(N), O(N) - Multiple loops though
# Approach is defined in editorial section video explanation
# https://practice.geeksforgeeks.org/problems/maximum-of-minimum-for-every-window-size3453/1
# To understand the last bit, just take the test case of "1 2 1 3"
def prevSmaller(arr):
    res = list()
    stack = list()
    for i in range(len(arr)):
        while len(stack)!=0 and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])

        stack.append(i)
    return res

def nextSmaller(arr):
    res = [0]*len(arr)
    stack = list()
    for i in range(len(arr)-1, -1, -1):
        while len(stack)!=0 and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if len(stack) == 0:
            res[i] = -1
        else:
            res[i] = stack[-1]

        stack.append(i)
    return res

class Solution:
    def maxOfMin(self,arr,n):
        prev = prevSmaller(arr)
        next = nextSmaller(arr)

        ans = [0] * (n+1)
        for i in range(n):
            length = next[i]-prev[i]-1
            ans[length] = max(ans[length], arr[i])

        for i in range(n-1, 0, -1):
            ans[i] = max(ans[i], ans[i+1])
        return ans[1:]