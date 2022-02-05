# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        def traverse(node, vals):
            if node:
                traverse(node.left, vals)
                traverse(node.right, vals)
                vals.append(node.val)
        res = []
        traverse(root, res)
        return res