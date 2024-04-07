#Diameter of Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SolutionNeet(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)
        dfs(root)
        return res[0]
    

class SolutionNeetComment(object):
    def diameterOfBinaryTree(self, root):
        def dfs(node): 
            nonlocal diameter
            if node is None: 
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            
            diameter = max(left + right, diameter)
            
            return max(left, right) + 1
        
        diameter = 0
        dfs(root)
        return diameter
        


node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)
    

#node2 = TreeNode(2)
#node1 = TreeNode(1, node2)
    
#node1 = TreeNode(1)
    
#node2 = TreeNode(2)
#node1 = TreeNode(1, None, node2)
#node3 = TreeNode(3, node1, None)

sol = SolutionNeetComment()
print(sol.diameterOfBinaryTree(node1))