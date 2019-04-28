# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        self.inorderTraversalNode(root, answer)
        return answer
        
    def inorderTraversalNode(self, node:TreeNode, answer):
        if node:
            self.inorderTraversalNode(node.left, answer)
            answer.append(node.val)
            self.inorderTraversalNode(node.right, answer)        
        
        
