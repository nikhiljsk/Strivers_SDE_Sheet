# Approach 1
# O(N), O(N)
class Solution:
    def dNums(self, nums, k):
        distCount = 0
        found = dict()
        for i in range(k):
            if nums[i] in found:
                found[nums[i]] += 1
            else:
                found[nums[i]] = 1
                distCount += 1


        ans=[distCount]
        for i in range(k, len(nums)):
            # Handle new element
            if nums[i] in found:
                if found[nums[i]] == 0:
                    distCount += 1
                found[nums[i]] += 1
            else:
                found[nums[i]] = 1
                distCount += 1

            # Handle the first element of the window
            if found[nums[i-k]] == 1:
                distCount -= 1
            found[nums[i-k]] -= 1
            
            ans.append(distCount)
        return ans