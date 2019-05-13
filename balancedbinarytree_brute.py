# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        if  root.left is None and root.right is None:
            return True
        
        if root.left and root.right:
            return abs(self._height(root.left)-self._height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        if root.left and root.right is None:
            return self._height(root.left) == 0
        
        if root.right and root.left is None:
            return self._height(root.right) == 0
        
        return False

        
    def _height(self, node):
        if node.left is None and node.right is None:
            return 0
        else:
            return 1+max((self._height(node.left) if node.left else 0), (self._height(node.right) if node.right else 0))
        
