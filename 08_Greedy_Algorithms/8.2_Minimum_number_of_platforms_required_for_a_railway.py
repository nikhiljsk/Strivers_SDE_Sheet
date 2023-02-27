# Approach 1
# O(N * LogN), O(1)
def minimumPlatform(self,n,arr,dep):
    if len(arr) == 1:
        return 1
    
    arr = sorted(arr)
    dep = sorted(dep)
    max_plat, curr_plat = 1, 1
    i, j = 1, 0
    while i < len(arr):
        if arr[i] <= dep[j]:
            curr_plat += 1
            i+=1
        elif arr[i] > dep[j]:
            curr_plat -= 1
            j+=1
        
        max_plat = max(max_plat, curr_plat)
    return max_plat