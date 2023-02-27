# Approach 1
# Fractional Knapsack
# O(N), O(1)
def fractionalknapsack(self, W,arr,n):
    arr = sorted(arr, reverse=True, key = lambda x: x.value/x.weight)

    max_p, curr_w = 0, 0
    for a in arr:
        if a.weight < W-curr_w:
            max_p += a.value
            curr_w += a.weight
        else:
            rem = W-curr_w
            max_p += ((rem)/a.weight)*(a.value)
            curr_w += rem
            break
    return max_p