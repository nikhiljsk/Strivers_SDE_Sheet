class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = dict()
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeNode(node)
            self.insertAtHead(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeNode(node)
            self.insertAtHead(node)
            node.value = value
            return
        
        if len(self.dic) >= self.cap:
            self.removeFromTail()
        node = ListNode(key,value)
        self.dic[key] = node
        self.insertAtHead(node)
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertAtHead(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
    
    def removeFromTail(self):
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeNode(tail_node)
        