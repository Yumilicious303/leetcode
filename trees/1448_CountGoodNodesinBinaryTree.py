#Count Good Nodes in Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        goodCount = 0
        def dfs(node, biggestinPath):
            nonlocal goodCount
            if node is None:
                return
            
            if node.val >= biggestinPath:
                goodCount += 1
            
            biggestinPath = max(node.val, biggestinPath)

            dfs(node.left, biggestinPath)
            dfs(node.right, biggestinPath)
        
        dfs(root, root.val)
        return goodCount
    
class Solution:
    def goodNodes(self, root: TreeNode):
        def dfs(node, maxVal):
            if node is None: return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            return res + dfs(node.left, maxVal) + dfs(node.right, maxVal)
        
        return dfs(root, root.val)
    



node3_2 = TreeNode(3)
node1_1 = TreeNode(1, node3_2)
node1_2 = TreeNode(1)
node5 = TreeNode(5)
node4 = TreeNode(4, node1_2, node5)
node3_1 = TreeNode(3, node1_1, node4)

sol = Solution()
print(sol.goodNodes(node3_1))
            
