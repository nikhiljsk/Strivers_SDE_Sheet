# Approach 1
# Roman to Integer
# O(N), O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
	    }

        prev, num = 0, 0
        for i in range(len(s)-1, -1, -1):
            curr = roman[s[i]]
            if prev > curr:
                num -= curr
            else:
                num += curr
            prev = curr
        return num

# Follow-up Question
# Integer to Roman
# O(Log10 N), O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [ ["I", 1],
                    ["IV", 4], ["V", 5],
                    ["IX", 9], ["X", 10],
                    ["XL", 40], ["L", 50],
                    ["XC", 90], ["C", 100],
                    ["CD", 400], ["D", 500],
                    ["CM", 900], ["M", 1000]
                ]

        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                num %= val
                res += (sym * count)
        return res