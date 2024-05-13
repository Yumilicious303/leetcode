#Binary Tree Zig Zag
from collections import deque
def zigzagLevelOrder(self, root):
    if root is None:
        return
    res, zigzagDirection = [], 1
    q = deque([root])
    while q:
        level, queueLength = [], len(q)
        for i in range(queueLength):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level = reversed(level) if len(res) % 2 else level
        res.append(level)
    return res