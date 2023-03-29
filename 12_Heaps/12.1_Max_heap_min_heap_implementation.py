import sys

class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*self.maxsize
        self.heap[0] = sys.maxsize * -1
        self.front = 0

    def parent(self, pos):
        return (pos-1) // 2

    def lChild(self, pos):
        return (2*pos)+1

    def rChild(self, pos):
        return (2*pos)+2

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def isLeafNode(self, pos):
        return 2*pos >= self.size

    def insert(self, val):
        if self.size >= self.maxsize:
            print("Overflow, ignore.")
            return

        self.heap[self.size] = val
        curr = self.size
        self.size += 1

        while self.heap[curr] < self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

    def remove(self):
        if self.size == 0:
            return

        if self.size == 1:
            self.size = 0
            return self.heap[0]

        val = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size-1]
        self.size -= 1
        self.minHeapify(self.front)
        return val

    def minHeapify(self, pos):
        if not self.isLeafNode(pos):
            if self.heap[pos] > self.heap[self.lChild(pos)] or self.heap[pos] > self.heap[self.rChild(pos)]:
                if self.heap[self.lChild(pos)] < self.heap[self.rChild(pos)]:
                    self.swap(pos, self.lChild(pos))
                    self.minHeapify(self.lChild(pos))
                else:
                    self.swap(pos, self.rChild(pos))
                    self.minHeapify(self.rChild(pos))

    def Print(self):
	    for i in range(0, (self.size//2)):
		    print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+
								str(self.heap[2 * i + 1])+" RIGHT CHILD : "+
								str(self.heap[2 * i + 2]))


# Max Heap
class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0]*self.maxsize
        self.heap[self.maxsize - 1] = sys.maxsize
        self.front = 0

    def parent(self, pos):
        return (pos-1) // 2

    def lChild(self, pos):
        return (2*pos)+1

    def rChild(self, pos):
        return (2*pos)+2

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def isLeafNode(self, pos):
        return 2*pos >= self.size

    def insert(self, val):
        if self.size >= self.maxsize:
            print("Overflow, ignore.")
            return

        self.heap[self.size] = val
        curr = self.size
        self.size += 1

        while self.heap[curr] > self.heap[self.parent(curr)]:
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)
        print("FIN", self.heap)

    def remove(self):
        if self.size == 0:
            return

        if self.size == 1:
            self.size = 0
            return self.heap[0]

        val = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size-1]
        self.size -= 1
        self.maxHeapify(self.front)
        return val

    def maxHeapify(self, pos):
        if not self.isLeafNode(pos):
            if self.heap[pos] < self.heap[self.lChild(pos)] or self.heap[pos] < self.heap[self.rChild(pos)]:
                if self.heap[self.lChild(pos)] > self.heap[self.rChild(pos)]:
                    self.swap(pos, self.lChild(pos))
                    self.maxHeapify(self.lChild(pos))
                else:
                    self.swap(pos, self.rChild(pos))
                    self.maxHeapify(self.rChild(pos))

    def Print(self):
	    for i in range(0, (self.size//2)):
		    print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+
								str(self.heap[2 * i + 1])+" RIGHT CHILD : "+
								str(self.heap[2 * i + 2]))

# Driver Code
if __name__ == "__main__":

    print('The minHeap is ')
    minHeap = MinHeap(9)
    minHeap.insert(1)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.insert(9)
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("The Min val is " + str(minHeap.remove()))
    print("\n\n\n")
    print('The maxHeap is ')
    maxHeap = MaxHeap(9)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)
    maxHeap.insert(9)
    maxHeap.Print()
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
    print("The Max val is " + str(maxHeap.remove()))
