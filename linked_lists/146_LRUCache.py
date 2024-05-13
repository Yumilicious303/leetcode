#LRU (Least Recently Used) Cache
class First_Try_Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class First_Try_LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.lru = None
        self.mru = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            if node.right:
                if node.left:
                    node.left.right = node.right
                    node.right.left = node.left
                    self.mru.right = node
                else:
                    self.lru = node.right
                    node.right.left = None
                node.left = self.mru
                self.mru.right = node
                node.right = None
                self.mru = node
            return node.value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self.dict[key].value = value
            self.get(key)
        else:
            node = Node(key, value)
            if len(self.dict) == 0:
                self.lru = node
                self.mru = node
                self.dict[key] = node
            elif len(self.dict) < self.capacity:
                self.mru.right = node
                node.left = self.mru
                self.mru = node
                self.dict[key] = node
            elif self.capacity == 1:
                self.dict.pop(self.lru.key)
                self.lru = node
                self.mru = node
                self.dict[key] = node
            else:
                self.dict.pop(self.lru.key)
                self.dict[key] = node

                self.lru = self.lru.right
                self.lru.left = None

                self.mru.right = node
                node.left = self.mru
                self.mru = node

class NodeNeet:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCacheNeet:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = NodeNeet(0, 0), NodeNeet(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = NodeNeet(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

class Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.left = self.right = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map key to node

        self.leftDummy, self.rightDummy = Node(), Node()
        self.rightDummy.left, self.leftDummy.right = self.leftDummy, self.rightDummy

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            newNode = Node(key, value)
            if len(self.cache) == self.capacity:
                leastRecentNode = self.leftDummy.right
                self.remove(leastRecentNode)
                del self.cache[leastRecentNode.key]
            self.cache[key] = newNode
            self.insert(newNode)

    # remove node from list
    def remove(self, node):
        leftNode, rightNode = node.left, node.right
        leftNode.right, rightNode.left = rightNode, leftNode

    # insert node at right
    def insert(self, node):
        leftNode = self.rightDummy.left
        leftNode.right = self.rightDummy.left = node
        node.left, node.right = leftNode, self.rightDummy



def case1():
    lruc = LRUCache(2)
    lruc.put(1,1)
    lruc.put(2,2)
    print(lruc.get(1))
    lruc.put(3, 3)
    print(lruc.get(2))
    lruc.put(4, 4)
    print(lruc.get(1))
    print(lruc.get(3))
    print(lruc.get(4))

def case14():
    lruc = LRUCache(2)
    lruc.put(2, 1)
    lruc.put(1, 1)
    lruc.put(2, 3)
    lruc.put(4, 1)
    print(lruc.get(1))
    print(lruc.get(2))

def case15():
    lruc = LRUCache(2)
    print(lruc.get(2))
    lruc.put(2, 6)
    lruc.get(1)
    lruc.put(1, 5)
    lruc.put(1, 2)
    print(lruc.get(1))
    print(lruc.get(2))


#case1()
#case14()
case15()