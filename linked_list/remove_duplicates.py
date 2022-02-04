# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head):
    if head is None:
        return head
    new_head = head
    tail = new_head
    while head.next:
        head = head.next
        if head.val != tail.val:
            tail.next = head
            tail = tail.next
    tail.next = None
    return new_head
