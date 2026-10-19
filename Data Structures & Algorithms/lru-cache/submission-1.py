class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #dummy nodes:
        #left.next is the least recently used node
        #right.prev is the most recently used node
        self.left = Node(0,0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

    def insert_at_end(self, node):
        previous = self.right.prev
        following = self.right

        previous.next = node
        node.prev = previous
        node.next = following
        following.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        #accessing the key makes it most recently used
        self.remove(node)
        self.insert_at_end(node)

        return node.value
    def put(self, key: int, value: int) -> None:
    #if key already exists, remove its old node
        if key in self.cache:
            self.remove(self.cache[key])

        #add the new node as most recently used
        node = Node(key, value)
        self.cache[key] = node
        self.insert_at_end(node)
        #if over capacity, remove the least recently used node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
