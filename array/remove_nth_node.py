'''
    Given a head of linked list and a number n.
    Delete nth node from the end of linked list.
    1 <= n <= len(Linked List) <= 30
'''

def remove_nth_from_end(head, n):
    if head.next is None:   # if linked list contains a single node, just remove it
        return None
    node, prev = head, None
    count = 1
    while node.next:
        if count < n:
            count += 1
        else:
            prev = head if prev is None else prev.next
        node = node.next
    if prev is None:    # means n==len(Linked list) so we remove first node
        head = head.next
    else:
        if n == 1:              # delete the last node
            prev.next = None    # previous of last's next is None
        else:
            prev.next = prev.next.next      # delete the node after the prev node
    return head                             # return the head of changed list