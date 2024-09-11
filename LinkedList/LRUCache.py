class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache_dict = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next 
        prv.next = nxt
        nxt.prev = prv
    
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prv
        prv.next = nxt.prev = node


    def get(self, key: int) -> int:
        if key in self.cache_dict:
            self.remove(self.cache_dict[key])
            self.insert(self.cache_dict[key])
            return self.cache_dict[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self.remove(self.cache_dict[key])
        self.cache_dict[key] = Node(key, value)
        self.insert(self.cache_dict[key])

        if len(self.cache_dict) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache_dict[LRU.key]
        
