class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    #hash map
    # doubly linked list
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0) #least recent
        self.right = Node(0, 0) #most recent
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node) -> None:
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self, node) -> None:
        prev_node, next_node = self.right.prev, self.right
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.insert(n)
            return n.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        
        if len(self.cache) > self.capacity:
            least = self.left.next
            self.remove(least)
            
            self.cache.pop(least.key)

            #void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
