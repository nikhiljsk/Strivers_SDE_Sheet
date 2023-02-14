# Approach 1
# O(N2), O(1)
class Solution:
    def countAndSay(self, n: int) -> str:
        output = '1'

        for i in range(2, n+1):
            res = ''
            prev = output[0]
            count = 1
            for x in output[1:]:
                if x == prev:
                    count += 1
                else:
                    res += str(count) + prev
                    count = 1
                    prev = x

            res += str(count) + prev
            output = res

        return output