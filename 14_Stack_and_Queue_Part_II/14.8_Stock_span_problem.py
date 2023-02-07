# Approach 1 Brute Force - TLE!
# O(N2), O(N)
class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        break_point = -1
        n = len(self.arr)
        for i in range(n-1,-1,-1):
            if self.arr[i] > price:
                break_point = i
                break
        self.arr.append(price)
        return n - break_point


# Approach 2
# O(2N), O(2N)
class StockSpanner:

    def __init__(self):
        self.stack = list()

    def next(self, price: int) -> int:
        res = 1
        while len(self.stack) != 0 and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res