# Approach 1
# Using two queues
from collections import deque

class MyStack:

    def __init__(self):
        self.q1, self.q2 = deque(), deque()
        

    def push(self, x: int) -> None:
        self.q2.append(x)
        while len(self.q1) != 0:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False


# Approach 1
# Using single queue
from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        for i in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False