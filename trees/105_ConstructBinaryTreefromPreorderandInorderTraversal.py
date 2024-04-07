#Construct Binary Tree from Preorder and Inorder Traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
    

sol = Solution()
#sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
sol.buildTree([7,-10,-4,3,-1,2,-8,11], [-4,-10,3,-1,7,11,-8,2])