from collections import deque
def rightSideView(root):
    res = []
    q = deque()
    if root: q.append(root)

    while q:
        res.append(q[0].val)
        for i in range(len(q)):
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
    return res


