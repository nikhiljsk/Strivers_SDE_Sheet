# Approach 1
# Using a min element
# O(1), O(2N)
class MinStack:

    def __init__(self):
        self.stack = list()
        self.minS = list()
        self.minElement = 2147483647

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minElement:
            self.minElement = val
        self.minS.append(self.minElement)

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()
        if len(self.minS) != 0:
            self.minElement = self.minS[-1]
        else:
            self.minElement = 2147483647

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minS[-1]


# Approach 2
# Without min element, cleaner code
# O(1), O(2N)
class MinStack:

    def __init__(self):
        self.stack = list()
        self.minS = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minS) != 0:
            self.minS.append(min(val, self.minS[-1]))
        else:
            self.minS.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minS[-1]


# Approach 3
# You could also insert pairs into one stack (curr_elem, so_far_found_minimum)
# instead of using two stack
# O(1), O(2N)


# Approach 4
# Optimal, O(1), O(N)
class MinStack:
    def __init__(self):
        self.stack = list()
        self.min = 2147483647

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.min = val
            return
        if val < self.min:
            self.stack.append((2*val-self.min))
            self.min = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        el = self.stack.pop()
        if el < self.min:
            self.min = (2*self.min)-el

    def top(self) -> int:
        el = self.stack[-1]
        if el < self.min:
            return self.min
        return el


    def getMin(self) -> int:
        return self.min