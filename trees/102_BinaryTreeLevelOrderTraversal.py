#Binary Tree Level Order Traversal
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        res = []
        def dfs(node, level):
            if node is None:
                return
            if len(res) < level + 1:
                res.append([])
            
            res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return res
    

class SolutionNeet:
    def levelOrder(self, root: TreeNode):
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        return res







node7 = TreeNode(7)
node15 = TreeNode(15)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
node3 = TreeNode(3, node9, node20)


sol = Solution()
print(sol.levelOrder(node3))