class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node5 = TreeNode(5)
node4 = TreeNode(4)
node3 = TreeNode(3)
node2 = TreeNode(2, node4, node5)
node1 = TreeNode(1, node2, node3)




def diameterOfBinaryTree(root):
    res = [0]
    def dfs(node):
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        res[0] = max(res[0], left + right)

        return 1 + max(left, right)
    dfs(root)
    return res[0]
    

print(diameterOfBinaryTree(node1))
