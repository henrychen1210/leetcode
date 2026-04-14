class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]

        self.removeNode(node)
        self.addNode(node, self.head, self.head.next)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.removeNode(node)
            self.addNode(node, self.head, self.head.next)
        else:
            node = Node(key, value)
            self.map[key] = node
            self.addNode(node, self.head, self.head.next)
            if len(self.map) > self.capacity:
                lastNode = self.tail.prev
                self.removeNode(lastNode)
                del self.map[lastNode.key]


    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def addNode(self, node, prevNode, nextNode):
        prevNode.next = node
        node.next = nextNode
        nextNode.prev = node
        node.prev = prevNode
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)