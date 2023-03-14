# Approach 1
# O(NLogN + N), O(1)
def findMinimumCoins(amount):
    d = sorted(denominations, reverse=True)
    coins, i, curr_sum = 0, 0, 0
    while curr_sum < amount:
        if d[i] <= amount-curr_sum:
            curr_sum += d[i]
            coins += 1
        else:
            i += 1
    return coins


# TODO Followup
# DP