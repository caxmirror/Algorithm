class Node:
    def __init__(self, key, value):
        self.key, self.val = key ,value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0) #LRU
        self.right = Node(0,0) #MRU
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cap += 1
        self.cache[key] = Node(key, value)
        if self.cap > 0:
            self.cap -= 1
            self.insert(self.cache[key])
        else:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            self.insert(self.cache[key])

    def insert(self, node): 
        prev = self.right.prev
        node.prev = prev
        prev.next = node
        node.next = self.right
        self.right.prev = node

    def remove(self, node): 
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev