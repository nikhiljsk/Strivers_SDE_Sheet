// Approach 1
// Copy both the arrays into new arrays, then sort the entire array, return kth
// O(NLogN), O(N)

// Approach 2
// Using two pointer approach to create new merged sorted array, then return kth
// O(N), O(N)

// Approach 3
// Similar to above approach, but just have a count, so as to not store the elements
// O(N), O(1)

// Approach 4
// Binary Search - O(LogN), O(1)
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)

        low = max(0, k-m)
        high = min(n, k)
        int_min, int_max = -2147483648, 2147483647

        while low <= high:
            cut1 = (low+high) >> 1
            cut2 = k-cut1

            if cut1 == 0:
                l1 = int_min
            else :
                l1 = arr1[cut1-1]

            if cut2 == 0:
                l2 = int_min
            else:
                l2 = arr2[cut2-1]

            if cut1 == n:
                r1 = int_max
            else:
                r1 = arr1[cut1]

            if cut2 == m:
                r2 = int_max
            else:
                r2 = arr2[cut2]

            if (l1<=r2) and (l2<=r1):
                return max(l1, l2)
            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1

        return -1