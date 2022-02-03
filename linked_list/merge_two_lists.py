# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_two_lists(list1, list2):
    '''
    list1 and list2 pointers to the head of each linked list
    '''
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        head, list1 = list1, list1.next
    else:
        head, list2 = list2, list2.next
    tail = head
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 if list2 is None else list2
    return head