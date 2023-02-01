class Queue :   
    def __init__(self, num):
        self.elements = [0]*num
        self.fronti, self.back = 0, 0
        self.curr_size = 0
        self.capacity = num

    def isEmpty(self) :
        if self.curr_size == 0:
            return True
        return False

    def enqueue(self, data) :
        if self.curr_size == self.capacity:
            print("\t! Queue full")
            return
        
        self.elements[self.back % self.capacity] = data
        self.back += 1
        self.curr_size += 1

    def dequeue(self) :
        if self.curr_size == 0:
            print("\t! Queue Empty")
            return -1
        tmp = self.elements[self.fronti % self.capacity]    
        self.fronti += 1
        self.curr_size -= 1
        return tmp

    def front(self) :
        if self.curr_size == 0:
            return -1
        return self.elements[self.fronti % self.capacity]


# Driver code
ob = Queue(3)
print("isEmpty:", ob.isEmpty())
print("Front is:", ob.front())
print("Inserting 1:")
ob.enqueue(1)
print("Inserting 2:")
ob.enqueue(2)
print("Front is:", ob.front())
print("Inserting 3:")
ob.enqueue(3)
print("Inserting 4:")
ob.enqueue(4)
print("Front is:", ob.front())
print("Try delete", ob.dequeue())
print("Inserting 4:")
ob.enqueue(4)
print("Try delete", ob.dequeue())
print("Front is:", ob.front())
print("isEmpty:", ob.isEmpty())
print("Try delete", ob.dequeue())
print("isEmpty:", ob.isEmpty())
print("Front is:", ob.front())
print("Try delete", ob.dequeue())
print("Front is:", ob.front())
print("Try delete", ob.dequeue())
