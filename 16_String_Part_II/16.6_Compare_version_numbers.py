# Approach 1
# Own Solution
# O(M+N), O(M+N)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rev1 = [s.lstrip("0") for s in version1.split(".")]
        rev2 = [s.lstrip("0") for s in version2.split(".")]

        m = min(len(rev1), len(rev2))
        i = 0
        while i < m:
            if rev1[i] == "" and rev2[i] == "":
                i += 1
                continue
            if rev1[i] == "":
                return -1
            if rev2[i] == "":
                return 1

            if int(rev1[i]) < int(rev2[i]):
                return -1
            if int(rev1[i]) > int(rev2[i]):
                return 1
            i += 1

        if len(rev1) < len(rev2):
            while i < len(rev2):
                if rev2[i] != "":
                    return -1
                i += 1

        if len(rev1) > len(rev2):
            while i < len(rev1):
                if rev1[i] != "":
                    return 1
                i += 1

        return 0


# Approach 2 - Cleaner code
# Own Solution
# O(M+N), O(M+N)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rev1 = version1.split(".")
        rev2 = version2.split(".")

        m, n = len(rev1), len(rev2)
        i, j = 0, 0

        # Padding with Zeros
        if m < n:
            rev1 += [0] * (n-m)
        if n < m:
            rev2 += [0] * (m-n)

        while i < max(m, n):
            if int(rev1[i]) < int(rev2[j]):
                return -1
            if int(rev1[i]) > int(rev2[j]):
                return 1

            i += 1
            j += 1

        return 0

# Approach 3
# O(M+N), O(1)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i, j = 0, 0

        while i < m or j < n:
            n1, n2 = 0, 0

            while i < m and version1[i] != ".":
                n1 = n1 * 10 + int(version1[i])
                i += 1

            while j < n and version2[j] != ".":
                n2 = n2 * 10 + int(version2[j])
                j += 1

            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
            i += 1
            j += 1

        return 0