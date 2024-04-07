class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot): return True
        return False
    
    def isSameTree(self, x, y):
        if x is None and y is None:
            return True
        if x is None or y is None or x.val != y.val:
            return False
        
        return self.isSameTree(x.left, y.left) and self.isSameTree(x.right, y.right)