from collections import defaultdict


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insertHead(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        self.size += 1

    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def removeTail(self):
        tail_prev = self.tail.prev
        self.removeNode(tail_prev)
        return tail_prev

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        self.freqTable = defaultdict(DLL)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.updateCache(key, self.cache[key].value)

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        if key in self.cache:
            self.updateCache(key, value)
            return
        if len(self.cache) == self.cap:
            prev_tail = self.freqTable[self.minFreq].removeTail()
            del self.cache[prev_tail.key]
        node = ListNode(key, value)
        self.freqTable[1].insertHead(node)
        self.cache[key] = node
        self.minFreq = 1

    def updateCache(self, key, value):
        node = self.cache[key]
        node.value = value
        prevFreq = node.freq
        node.freq += 1
        self.freqTable[prevFreq].removeNode(node)
        self.freqTable[node.freq].insertHead(node)

        if prevFreq == self.minFreq and self.freqTable[prevFreq].size == 0:
            self.minFreq += 1
        return node.value