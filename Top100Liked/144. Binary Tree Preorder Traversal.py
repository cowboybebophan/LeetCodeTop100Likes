"""
Similar to problem 94 and 145.
"""

# Iterratively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                root = tmpNode.right
        return res
                
# Recursively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
                   
