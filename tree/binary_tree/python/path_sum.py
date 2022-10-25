'''
Given the root of a binary tree and an integer targetSum, 
    return true if the tree has a root-to-leaf path 
    such that adding up all the values along the path equals targetSum.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # algorithm 1
        '''
        if not root:
            return False
        sums = set()
        def paths(node, s, can):
            if not node:
                return
            if not node.left and not node.right:
                can += node.val
                s.add(can)
                return
            if node.left:
                paths(node.left, s, can+node.val)
            if node.right:
                paths(node.right, s, can+node.val)
        
        paths(root, sums, 0)
        # print(sums)
        if targetSum in sums:
            return True
        return False
        '''

        # algorithm 2
        if not root:
            return False
        def hasPath(node, s):
            ans = False
            subSum = s - node.val
            if subSum == 0 and node.left is None and node.right is None:
                return True
            if node.left:
                ans = ans or hasPath(node.left, subSum)
            if node.right:
                ans = ans or hasPath(node.right, subSum)
            return ans
        return hasPath(root, targetSum)