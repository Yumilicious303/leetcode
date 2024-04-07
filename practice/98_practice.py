# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def dfs(node, leftBound, rightBound):
            if node is None:
                return True
            if node.val <= leftBound or node.val >= rightBound:
                return False
            
            return dfs(node.left, leftBound, node.val) and dfs(node.right, node.val, rightBound)

        return dfs(root, float('-inf'), float('inf'))