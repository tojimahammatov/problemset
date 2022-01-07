'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
'''

# class ListNode:
#     def __init__(self, value, next) -> None:
#         self.value = value 
#         self.next = next 

# two pointers are good to go, we move twice as we preserve middle by moving one
def middle_node(head):
    slow, fast = head, head
    while fast:
        if fast.next == None:
            return slow
        else:
            slow = slow.next
            fast = fast.next.next
    return slow