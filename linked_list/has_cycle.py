'''
    Given is a linked-list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head) -> bool:
    if head is None or head.next is None:
        return False
    head.accessed_before = True
    while head.next:
        head = head.next
        if hasattr(head, 'accessed_before'):
            return True
        head.accessed_before = True
    return False