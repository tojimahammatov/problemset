# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    2           2
   / \    =>   / \
  1   3       3   1
'''

class Solution:
    def invertTree(self, root):
        def invert(parent):
            if parent==None:
                return
            if parent.left!=None or parent.right!=None:
                parent.left, parent.right = parent.right, parent.left
                invert(parent.left)
                invert(parent.right)
            return
        invert(root)
        return root