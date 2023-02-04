# Approach 1
# O(Log2 (M*)) - Where d is the number of decimals
def NthRoot(self, n, m):
    if m<=1:
        return 1
    l, r = 1, m
    while l<=r:
        mid = l+((r-l)//2)
        mid_square = mid**n
        if mid_square < m:
            l = mid+1
        elif mid_square > m:
            r = mid-1
        else:
            return mid
    return -1

# If the question was to find to the decimal
# O(Log2 (M*10**d)) - Where d is the number of decimals