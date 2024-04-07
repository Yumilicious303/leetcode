#Balanced Binary Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            nonlocal balanced
            if node is None or balanced is False:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(right - left) <= 1:
                balanced = False

            return 1 + max(left, right)
        balanced = True
        dfs(root)
        return balanced


class SolutionNeet(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]            
    

node15 = TreeNode(15)
node7 = TreeNode(7)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9)
node3 = TreeNode(3, node9, node20)

sol = SolutionNeet()
print(sol.isBalanced(node3))