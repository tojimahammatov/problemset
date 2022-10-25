'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res
        def paths(node, s):
            if node.left is None and node.right is None:
                s = s + str(node.val)
                res.append(s)
                return
            if node.left:
                paths(node.left, s + str(node.val) + "->")
            if node.right:
                paths(node.right, s + str(node.val) + "->")
                
        paths(root, "")
        return res