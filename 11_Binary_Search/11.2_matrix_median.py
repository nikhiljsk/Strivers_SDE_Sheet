# Approach 1 - Brute Force
# O(NLogN), O(N)
# We could copy over all the array elements in a new 1d array, sort the array and return middle

# Approach 2
# O(max_int * NLogN), O(1)
# Take a number range, and keep searching on how many numbers exists
# in the matrix before and after that mid.
def countSmaller(arr, target):
    l, r = 0, len(arr)-1
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] <= target:
            l = mid+1
        else:
            r = mid-1
    return l

class Solution:
    def median(self, matrix, R, C):
        l, r = 0, 2000
        while l<=r:
            mid = l + (r-l)//2

            count = 0
            for i in range(R):
                count += countSmaller(matrix[i], mid)

            target = (R*C)//2
            if count <= target:
                l = mid+1
            else:
                r = mid-1
        return l