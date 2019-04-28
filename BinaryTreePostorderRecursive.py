# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        answer = []
        self.postorderTraversalNode(root, answer)
        return answer
        
    def postorderTraversalNode(self, node: TreeNode, answer):
        if node:
            self.postorderTraversalNode(node.left, answer)
            self.postorderTraversalNode(node.right, answer)
            answer.append(node.val)
        
        
