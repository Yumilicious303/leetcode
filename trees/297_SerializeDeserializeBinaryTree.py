#Serialize Binary Tree
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecNeet:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
    

class CodecBFS:
    def serialize(self, root):
        # use level order traversal to match LeetCode's serialization format
        res = []
        queue = deque([root])
        while queue:
            node = queue.pop()
            if node:
                res.append(str(node.val))
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            else:
                # you can use any char to represent null
                # empty string means test for a non-null node is simply: flat_bt[i]
                res.append('N')
        return ','.join(res)
    # time:  O(n)
    # space: O(n)

    def deserialize(self, data):
        if not data or data[0] == 'N':
            return
        values = data.split(',')
        res = TreeNode(values[0])
        queue = deque([res])
        i = 1
        # when you pop a node, its children will be at i and i+1
        while queue:
            node = queue.pop()
            if i < len(values) and values[i] != 'N':
                node.left = TreeNode(int(values[i]))
                queue.appendleft(node.left)
            i += 1
            if i < len(values) and values[i] != 'N':
                node.right = TreeNode(int(values[i]))
                queue.appendleft(node.right)
            i += 1
        return res
    # time:  O(n)
    # space: O(n)