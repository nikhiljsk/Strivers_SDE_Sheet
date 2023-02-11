# Approach 1
# Sort the array amd for each distance from [1, maxDistance], check if is compatible.
# If yes, then increment dist by one, else break and return
# O(M*N), O(1)

# Approach 2
# O(NLogN), O(1)
def isPossible(nums, k, mid):
    count, last_place = 1 ,nums[0]
    for v in nums:
        if v-last_place >= mid:
            last_place = v
            count += 1
    if count >= k:
        return True
    return False


class Solution:
    def solve(self,n,k,stalls):
        stalls = sorted(stalls)
        low, high = 1, stalls[-1]-stalls[0]

        res = 0
        while low <= high:
            mid = (low+high) >> 1
            if isPossible(stalls, k, mid):
                res = mid
                low = mid + 1
            else:
                high = mid-1
        return res