# Approach 1 - TLE!
# O(N3), O(1)
def isPalindrome(s) -> bool:
    l, r = 0, len(s)-1
    while l < len(s) and r >= 0:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = s[0], 1
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if j-i+1 > resLen and isPalindrome(s[i:j+1]):
                    resLen = j-i+1
                    res = s[i:j+1]
        return res

# Approach 2
# O(N2), O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            # Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

            # Even Length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res

# TODO DP