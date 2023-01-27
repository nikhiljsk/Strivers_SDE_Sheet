# Approach 1
# O(N * LogN), O(N)
def maximumActivities(start, finish):
    times = list()
    for i, j in zip(start, finish):
        times.append([i, j])

    # Sort based on end time
    times = sorted(times,key=lambda x: x[1])

    # Calculate
    res = 1
    s, e = times[0][0], times[0][1]
    for i, j in times:
        if e <= i:
            res += 1
            s, e = i, j
    return res