# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head):
    if head is None or head.next is None:
        return head
    stack = [head]
    while head.next:
        stack.append(head.next)
        head = head.next
    new_head = stack.pop()
    tail = new_head
    while len(stack)>0:
        tail.next = stack.pop()
        tail = tail.next
    tail.next = None
    return new_head
