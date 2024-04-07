class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p2 = TreeNode(2)
p3 = TreeNode(3)
p1 = TreeNode(1, p2, p3)

q2 = TreeNode(2)
q3 = TreeNode(3)
q1 = TreeNode(1, q2, q3)


r2 = TreeNode(2)
r1 = TreeNode(1, r2)

s2 = TreeNode(2)
s1 = TreeNode(1, None, r2)


x2 = TreeNode(2)
x3 = TreeNode(3)
x1 = TreeNode(1, x2, x3)

y2 = TreeNode(2)
y4 = TreeNode(4)
y1 = TreeNode(1, y2, y4)


def isSameTree(p, q):
    if q is None and p is None:
        return True
    if (p and not q) or (q and not p):
        return False
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

print(isSameTree(p1, q1))
print(isSameTree(s1, r1))
print(isSameTree(x1, y1))