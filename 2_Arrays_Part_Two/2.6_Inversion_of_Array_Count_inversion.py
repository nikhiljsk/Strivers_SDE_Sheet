# Python - TLE!
# O(N2), O(1)
def inversionCount(self, arr, n):
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                c+=1
    return c



# Approach 2
# Merge sort
# O(N * LogN), O(N)
class Solution:
    def merge(self, arr, left, mid, right, temp_arr):
        i, j, k = left, mid+1, left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i+=1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid-i + 1)
                j+=1
            k+=1
        
        while i <= mid:
            temp_arr[k] = arr[i]
            i+=1
            k+=1
            
        while j <= right:
            temp_arr[k] = arr[j]
            j+=1
            k+=1
        
        for i in range(left, right+1):
            arr[i] = temp_arr[i]
        
        return inv_count


    def mergeSort(self, arr, left, right, temp_arr):
        inv_count = 0
        if left < right:
            mid = (left+right)//2
            inv_count += self.mergeSort(arr, left, mid, temp_arr)
            inv_count += self.mergeSort(arr, mid+1, right, temp_arr)
            inv_count += self.merge(arr, left, mid, right, temp_arr)
        return inv_count
    
    
    def inversionCount(self, arr, n):
        temp_arr = [0]*n
        return self.mergeSort(arr, 0, n-1, temp_arr)