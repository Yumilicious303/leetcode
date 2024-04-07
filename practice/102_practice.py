from collections import deque
def levelOrder(root):
    res = []
    q = deque([root])
    while q:
        level = []
        for i in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            q.append(node.left)
            q.append(node.right)
        res.append(level.copy())
    return res

