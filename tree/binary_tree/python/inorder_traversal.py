# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        def traverse(node, vals):
            if node:
                traverse(node.left, vals)
                vals.append(node.val)
                traverse(node.right, vals)
        res = []
        traverse(root, res)
        return res