#Copy List with Random Pointer
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        return str(self.val, self.random)

def copyRandomList(head):
    oldtoNew = {}
    def dfs(node):
        if node is None:
            return None
        
        if node in oldtoNew:
            return oldtoNew[node]
        
        copy = Node(node.val)
        oldtoNew[node] = copy

        copy.random = dfs(node.random)
        copy.next = dfs(node.next)

        return copy
    
    return dfs(head)

def copyRandomList(head):
    oldtoCopy = {None: None}

    cur = head 
    while cur:
        copy = Node(cur.val)
        oldtoCopy[cur] = copy
        cur = cur.next
    
    cur = head
    while cur:
        copy = oldtoCopy[cur]
        copy.next = oldtoCopy[cur.next]
        copy.random = oldtoCopy[cur.random]
        cur = cur.next
    
    return oldtoCopy[head]






node7 = Node(7)
node13 = Node(13)
node11 = Node(11)
node10 = Node(10)
node1 = Node(1)


node7.next = node13
node13.next = node11
node11.next = node10
node10.next = node1


node13.random = node7
node11.random = node1
node10.random = node11
node1.random = node7




copyRandomList(node7)