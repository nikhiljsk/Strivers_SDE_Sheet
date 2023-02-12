# Approach 1
# O(N), O(1) - Where N is the number of characters
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for new_string in strs:
                if len(new_string) == i or new_string[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res