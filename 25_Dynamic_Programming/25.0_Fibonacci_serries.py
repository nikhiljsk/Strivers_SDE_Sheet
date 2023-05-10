# Approach 1
# Recursion
# O(2^N), O(N)
class Solution:
    def helper(self, n):
        if n <= 1:
            return n
        return self.helper(n-1) + self.helper(n-2)

    def fib(self, n: int) -> int:
        return self.helper(n)

# Approach 2
# Memoization
# O(N), O(2N)
class Solution:
    def helper(self, n, dp):
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.helper(n-1, dp) + self.helper(n-2, dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        return self.helper(n, dp)

# Approach 3
# Tabulation
# O(N), O(N)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [-1 for _ in range(n+1)]
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

# Approach 4
# Optimized Space for DP
# O(N), O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        p1, p2, res = 0, 1, 0
        for i in range(2, n+1):
            res = p1+p2
            p1 = p2
            p2 = res
        return res