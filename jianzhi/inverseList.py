from ListNode import ListNode

def inverse(head, newHead):
    if head is None:
        return
    if head.next is None:
        newHead = head
        return newHead
    else:
        newHead=inverse(head.next, newHead)
        head.next.next = head
        head.next = None
        return newHead

head = ListNode(1)
head_point = head
for i in range(2, 5):
    head.addNext(i)
    head = head.next



head_point.show()
head_point = inverse(head_point, head_point)
head_point.show()

