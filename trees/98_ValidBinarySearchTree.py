# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(node, leftBound, rightBound):
            if node is None:
                return True

            if node.val <= leftBound or node.val >= rightBound:
                return False

            return valid(node.left, leftBound, node.val) and valid(node.right, node.val, rightBound)

        return valid(root, float("-inf"), float("inf"))