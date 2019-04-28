# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        self.preorderTraversalNode(root, answer)
        return answer
        
    def preorderTraversalNode(self, node: TreeNode, answer):
        if node:
            answer.append(node.val)
            self.preorderTraversalNode(node.left, answer)
            self.preorderTraversalNode(node.right, answer)
            
        
        
