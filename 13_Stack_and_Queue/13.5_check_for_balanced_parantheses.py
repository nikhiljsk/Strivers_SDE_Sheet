# Approach 1
# O(N), O(N)
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        openPairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        closePairs = {v: k for k, v in openPairs.items()}

        stack = deque()
        for i in range(len(s)):
            if s[i] in openPairs.keys():  # Means open bracket
                stack.append(s[i])
            else: # Means closed bracket
                if len(stack)==0:
                    return False
                if stack.pop() != closePairs[s[i]]:
                    return False
        if len(stack) == 0:
            return True
        return False