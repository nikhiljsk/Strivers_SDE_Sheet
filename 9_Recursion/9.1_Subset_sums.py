# Approach 1
# O(2**N + Sorting), O(2**N)
def helper(self, arr, ind, summ, res):
    if ind == len(arr):
        res.append(summ)
        return
    
    # Include
    self.helper(arr, ind+1, summ+arr[ind], res)
    
    # Exclude
    self.helper(arr, ind+1, summ, res)
    
    return res


def subsetSums(self, arr, N):
    res = list()
    return self.helper(arr, 0, 0, res)