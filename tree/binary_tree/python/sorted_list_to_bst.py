'''
Given an integer array nums where the elements are sorted in ascending order, 
    convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree 
    in which the depth of the two subtrees of every node never differs by more than one.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def sortedListToBST(nums):
    if not nums:
        return None

    middle = len(nums) // 2
    root = TreeNode(middle)
    root.left = sortedListToBST(nums[:middle])
    root.right = sortedListToBST(nums[middle+1:])
    return root