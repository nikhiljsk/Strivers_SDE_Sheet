# Approach 1
# O(N * LogN), O(N)
def maximumMeetings(self,n,start,end):
    times = list()
    for i, j in zip(start, end):
        times.append([i, j])

    # Sort based on end time
    times = sorted(times,key=lambda x: x[1])

    # Calculate
    res = 1
    s, e = times[0][0], times[0][1]
    for i, j in times:
        if e < i:
            res += 1
            s, e = i, j
    return res

# Approach 2
# If meeting number is asked to be retured, store the index
# O(N * LogN), O(N)
def maximumMeetings(start, end):
    times = list()

    ind = 1
    for i, j in zip(start, end):
        times.append([i, j, ind])
        ind += 1

    # Sort based on end time
    times = sorted(times, key=lambda x: x[1])
    # Calculate
    res = [times[0][2]]
    _, e = times[0][0], times[0][1]
    for i, j, k in times:
        if e < i:
            res.append(k)
            _, e = i, j
    return res
