# 24/11/7
class Node:
    def __init__(self, key, val):
        self.nex = None
        self.pre = None
        self.val = val
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # key: data # val: Node
        self.cap = capacity
        self.left = Node(0,0) #recently used
        self.right = Node(0,0) #not recently used
        self.left.nex = self.right
        self.right.nex = None
        self.left.pre = None
        self.right.pre = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            self.cache[key].val = value
        else: 
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            self.cap -= 1
            print(self.cap)
            if self.cap < 0:
                delnode = self.right.pre
                self.delete(delnode)
                del self.cache[delnode.key]
                self.cap += 1
            
            
    def delete(self, node):
        node_pre = node.pre
        node_nex = node.nex
        node_pre.nex = node_nex
        node_nex.pre = node_pre
    def insert(self, node):
        self.left.nex.pre = node
        node.nex = self.left.nex
        node.pre = self.left
        self.left.nex = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

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