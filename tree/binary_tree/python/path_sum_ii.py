'''
Given the root of a binary tree and an integer targetSum, 
    return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        def paths(node, r, s):
            subSum = s - node.val
            if subSum == 0 and node.left is None and node.right is None:
                r.append(node.val)
                res.append(r)
            if node.left:
                paths(node.left, r + [node.val], subSum)
            if node.right:
                paths(node.right, r + [node.val], subSum)
                
        paths(root, [], targetSum)
        return res