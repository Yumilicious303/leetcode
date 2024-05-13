#Kth Smallest Element in a Binary Search Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.val)
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


def testCase1():
    node2 = TreeNode(2)
    node1 = TreeNode(1, None, node2)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node1, node4)
    sol = SolutionNeet()
    print(sol.kthSmallest(node3, 1))

def testCase2():
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node2, node4)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node3, node6)
    sol = SolutionNeet()
    print(sol.kthSmallest(node5, 4))

testCase2()