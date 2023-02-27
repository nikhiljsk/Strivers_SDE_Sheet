# Approach 1
# O(N2), O(1)
def maxLen(self, n, arr):
    max_len = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == 0:
                max_len = max(max_len, j-i+1)
    return max_len


# Approach 2
# O(N), O(N)
def maxLen(self, n, arr):
    # Storing prefix sum and the index is the important factor here
    prefix_sum = dict()
    max_len, curr_sum = 0, 0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = max(max_len, i+1)
        if curr_sum not in prefix_sum.keys():
            prefix_sum[curr_sum] = i
        else:
            max_len = max(max_len, i-prefix_sum[curr_sum])
    return max_len