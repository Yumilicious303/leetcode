#Kth Smallest Element in a Binary Search Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        order = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)

        dfs(root)
        return order[k - 1]

class SolutionNeet(object):
    def kthSmallest(self, root, k):
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right



node2 = TreeNode(0)
node1 = TreeNode(1, node2)
node4 = TreeNode(4)
node3 = TreeNode(3, node1, node4)