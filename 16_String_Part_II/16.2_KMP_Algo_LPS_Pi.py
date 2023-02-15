# Approach 1
# O(N2), O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        m, n = len(needle), len(haystack)
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1

# Approach 2
# Rabin Karp
# O(N-M+1) Average, O(NM) Worst case, O(1) Space
class Solution:
    def strStr(self, s: str, p: str) -> int:
        if len(p) > len(s):
            return -1

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
                    return i
            if i < n-m:
                hash_s = (d*(hash_s-ord(s[i])*h)+ord(s[i+m])) % q
        return -1


# Approach 3
# KMP Algorithm - Kunth Morris Pratt
# O(M+N), O(M)
# Refer: https://www.youtube.com/watch?v=JoF0Z7nVSrA&ab_channel=NeetCode
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1