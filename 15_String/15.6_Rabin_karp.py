# Rabin Karp
# O(N-M+1) Average, O(NM) Worst case where pattern is "aa" and string is "aaaaa", O(1) Space
# Refer for explanation: https://www.youtube.com/watch?v=qQ8vS2btsxI&ab_channel=AbdulBari
def stringMatch(s, p):
    d, q = 26, 100000
    n = len(s)
    m = len(p)
    h = pow(d, m-1) % q
    hash_p = 0
    hash_s = 0
    output = []
    for i in range(m):
        hash_p = (d*hash_p + ord(p[i])) % q
        hash_s = (d*hash_s + ord(s[i])) % q
    for i in range(n-m+1):
        if hash_s == hash_p:
            if s[i:i+m] == p:
                output.append(i)
        if i < n-m:
            hash_s = (d*(hash_s-ord(s[i])*h)+ord(s[i+m])) % q
    return output
