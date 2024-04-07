#Clone Graph
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return str(self.val)


def cloneGraph(node):
    nodeMap = {}
    def dfs(curNode):
        if curNode in nodeMap:
            return 
        
        nodeClone = Node(curNode.val)
        nodeMap[curNode] = nodeClone

        for n in curNode.neighbors:
            if n in nodeMap:
                nodeClone.neighbors.append(nodeMap[n])
            else:
                dfs(n)
                nodeClone.neighbors.append(nodeMap[n])
    dfs(node)
    print('yolo')
    return nodeMap[node] if node else None


def cloneGraphNeet(node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    
    return dfs(node) if node else None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print(cloneGraphNeet(node1))

