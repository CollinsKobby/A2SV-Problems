def insertNodeAtTail(head, data):
    lst = SinglyLinkedListNode(data)
    if head is None:
        return lst
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = lst
    return head