'''
Given the root of a binary tree and an integer targetSum, 
    return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, 
    but it must go downwards (i.e., traveling only from parent nodes to child nodes).
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        hit = []
        # dfs traverse tree
        def dfs(root,target) :
            if root :
                dfs(root.left,target)
                dfs(root.right,target)
                find_path(root,target)

        def find_path(root,target) :
            if root :
                n = target - root.val
                if n==0 : hit.append(1)
                find_path(root.left,n)
                find_path(root.right,n)
                
        dfs(root,targetSum)
        return sum(hit)
        '''
        
        res = []
        if not root:
            return 0
        def dfs(node, s):
            if node:
                dfs(node.left, s)
                dfs(node.right, s)
                paths(node, s)

        def paths(node, s):
            subSum = s - node.val
            if subSum == 0:
                res.append(1)
            if node.left:
                paths(node.left, subSum)
            if node.right:
                paths(node.right, subSum)
                
        dfs(root, targetSum)
        return len(res)