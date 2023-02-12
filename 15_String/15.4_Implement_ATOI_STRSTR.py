# Approach 1
# Pythonic Way
# O(N), O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        isNeg = False
        if s[0] == "-":
            isNeg = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        num = ""
        for i in s:
            if not i.isdigit():
                break
            num += i

        if len(num) == 0:
            return 0

        num = int(num)

        if isNeg and num > 2147483647:
            return -2147483648
        if num > 2147483647:
            return 2147483647
        if isNeg:
            return -1 * num
        return num

# Approach 2
# Other languages, mostly the same, but a few things change.
"""
if (res > max/10) || (res == max/10 && r > 7) || (res < min/10) || (res == min/10 && r < -8) {
			if negative == -1 {
				return min
			} else {
				return max
			}
		}
		res = (res * 10) + r
"""