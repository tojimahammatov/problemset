# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def remove_elements(head, val: int):
    new_head = None
    current = None
    while head:
        if head.val != val:
            # node = head
            if current:
                current.next = head
                current = current.next
            else:
                new_head = head
                current = head
        head = head.next
    if current and current.next and current.next.val == val:
        current.next = None
    return new_head