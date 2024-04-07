class Node:
    def __init__(self, key = None, value = None, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dcty = {}
        self.mRU, self.lRU = Node(), Node()
        self.mRU.left = self.lRU
        self.lRU.right = self.mRU

    def get(self, key: int) -> int:
        if key in self.dcty: 
            node = self.dcty[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dcty:
            node = self.dcty[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = Node(key, value)
            self.dcty[key] = new_node
            if len(self.dcty) > self.capacity:
                deleted_node = self.lRU.right
                self.remove(deleted_node)
                del self.dcty[deleted_node.key]
            self.insert(new_node)
            
    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left
    
    def insert(self, node):
        left = self.mRU.left

        left.right = node
        self.mRU.left = node

        node.left = left
        node.right = self.mRU





lru_cache = LRUCache(2)
print(lru_cache.put(1, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(1))
print(lru_cache.put(3, 3))
print(lru_cache.get(2))
print(lru_cache.put(4, 4))
print(lru_cache.get(1))
print(lru_cache.get(3))
print(lru_cache.get(4))