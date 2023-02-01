# Stack class.
class Stack:

    def __init__(self, capacity: int):
        self.elements = list()
        self.topi = -1
        self.capacity = capacity

    def push(self, num: int) -> None:
        print("Inserting:", num)
        self.elements.append(num)
        self.topi = len(self.elements)-1

    def pop(self) -> int:
        if len(self.elements) > 0:
            self.topi -= 1
            return self.elements.pop()
        self.topi = -1
        return -1

    def top(self) -> int:
        if self.topi == -1:
            return -1
        return self.elements[self.topi]

    def isEmpty(self) -> int:
        if len(self.elements) == 0:
            return 1
        return 0

    def isFull(self) -> int:
        if len(self.elements) >= self.capacity:
            return 1
        return 0

# Driver code
ob = Stack(3)
print("isEmpty:", ob.isEmpty())
print("Top is:", ob.top())
ob.push(1)
ob.push(2)
ob.push(3)
print("isFull:", ob.isFull())
print("Top is:", ob.top())
print("Try delete", ob.pop())
print("Try delete", ob.pop())
print("isEmpty:", ob.isEmpty())
print("Try delete", ob.pop())
print("isEmpty:", ob.isEmpty())
print("Try delete", ob.pop())