#Binary Tree Right Side
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    res = []
    if root:
        q = deque()
        q.append(root)
        while q:
            res.append(q[0].val)
            for i in range(len(q)):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
    return res

def rightSideViewNeet(root):
    res = []
    q = deque([root])

    while q:
        rightSide = None
        qLen = len(q)

        for i in range(qLen):
            node = q.popleft()
            if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            res.append(rightSide.val)
    return res


node4 = TreeNode(4)
node5 = TreeNode(5, node4)
node2 = TreeNode(2, None, node5)

node6 = TreeNode(6)
node3 = TreeNode(3, node6)

node1 = TreeNode(1, node2, node3)

print(rightSideView(node1))
print(rightSideView(None))

print(rightSideViewNeet(node1))
print(rightSideViewNeet(None))
