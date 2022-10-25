# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Ex:
'''
Input: [3, 9, 20, null, null, 15, 7]
            3
          /   \
         9     20
              /  \
             15   7

Output: [[3], [9, 20], [15, 7]]          
'''


class Solution:
    def levelOrder(self, root):
        if not root:
            return root
        res = []
        queue = [(root, 1)]
        while queue:
            node, depth = queue.pop(0)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
        return res


# using a deque of collections library for building a queue

from collections import deque

class Solution2:
    def levelOrder(self, root):
        if not root:
            return root
        res = []
        queue = deque([(root, 1)])          # only change to make a queue
        while queue:
            node, depth = queue.popleft()   # O(1) time
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
            if len(res) < depth:
                res.append([])
            res[depth-1].append(node.val)
        return res
