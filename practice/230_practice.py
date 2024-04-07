def kthSmallest(root, k):
    n = 0
    def dfs(node):
        nonlocal n
        if node is None: return -1
        left = dfs(node.left)
        if left >= 0: return left
        n += 1
        if n == k: return node.val
        right = dfs(node.right)
        if right >=  0: return right
        return -1
    return dfs(root)


def kthSmallestIterative(root, k):
    n = 0
    cur = root
    stack = []
    while True:
        if cur is None:
            cur = stack.pop()
            continue
