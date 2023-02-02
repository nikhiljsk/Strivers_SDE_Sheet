# Approach 1
# Using 2 Stack
from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False

# Approach 2
# Amortized O(1)
from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        return False