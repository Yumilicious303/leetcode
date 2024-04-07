# Subtree of Another Tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, node, subNode):
        if node is None and subNode is None:
            return True
        
        if node is None or subNode is None or node.val != subNode.val:
            return False
        
        return self.isSameTree(node.left, subNode.left) and self.isSameTree(node.right, subNode.right)


class SolutionNeet(object):
    def isSubtree(self, root, subRoot):
        if subRoot is None: return True
        if root is None: return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, s, t):
        if s is None and t is None:
            return True
        
        if s is None or t is None or s.val != t.val:
            return False
        
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)